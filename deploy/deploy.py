#!/usr/bin/env python
import argparse
import time
import datetime
import os
import json
import sys
import subprocess
import logging
from pprint import pformat


class Deploy(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self, **kwargs):
        # Defaults
        self.__dict__.update(colorize=True,
                             basedir="",
                             tag=False,
                             executable=None,
                             config="deploy.json",
                             venv_dir=None,
                             extra_requirements=[],
                             cachedir="pipcache",
                             wheeldir="wheelhouse",
                             repo_dir="repo",
                             package=None,
                             rev="HEAD",
                             venv_name_command="git --git-dir {repo_dir}/.git --no-pager log -1 --format='%f' {rev}",
                             )
        # Override from kwargs
        fail = bool(kwargs.get('config') != self.config)
        self.__dict__.update(kwargs)

        try:
            self.__dict__.update(json.load(open(self.config)))
        except Exception as e:
            if fail:
                self.fail("Failed to load config file {}".format(self.config), 5, exception=e)
            self.warn("Failed to load config file {}".format(self.config))

        # Finally, kwargs take priority over config, so apply again
        self.__dict__.update(kwargs)

        # ---- Process configurations
        # For each othe the other directories, join to basedir if a non-abs
        # path is specified
        if not os.path.isabs(self.cachedir):
            self.cachedir = os.path.realpath(os.path.join(self.basedir, self.cachedir))

        if not os.path.isabs(self.wheeldir):
            self.wheeldir = os.path.realpath(os.path.join(self.basedir, self.wheeldir))

        if not os.path.isabs(self.repo_dir):
            self.repo_dir = os.path.realpath(os.path.join(self.basedir, self.repo_dir))

        if self.package is None:
            self.fail("A package name must be provided!")
        if self.executable is None:
            self.fail("An executable name is required")

        # ---- Setup base information
        self.basedir = os.path.realpath(self.basedir)

        self.logger.debug("Deploy config:\n{}".format(pformat(self.__dict__)))

    def color(self, string, color):
        """ Colorize an output string if coloring is enabled """
        if self.colorize:
            return color + string + self.ENDC
        else:
            return string

    def req(self, command_string):
        """ Require the call to succeed, or exit """
        ret = self.system(command_string)
        if ret:
            self.fail("Command {} exited with return code {}"
                      .format(command_string, ret), ret * -1)

    def warn(self, message):
        self.logger.warn(self.color("!! {}".format(message), self.HEADER))

    def fail(self, message, code=5, exception=None):
        # XXX: Print exception information
        self.logger.error(self.color("#### ERROR: {} ####".format(message), self.WARNING))
        exit(code)

    def system(self, call, output=False):
        """ Simple wrapper for os.system that prints the command that's being
        executed """
        self.logger.info(self.color("-- {}".format(call), self.OKBLUE))
        if output:
            try:
                return subprocess.check_output(call, shell=True).strip()
            except subprocess.CalledProcessError as e:
                self.fail("Command {} exited with return code {}"
                          .format(call, e.returncode), e.returncode * -1)
        return os.system(call)

    def try_pip(self, pip_fragment):
        """ Runs a pip fragment which will first try to install from the
        wheelhouse. If it fails to install everything from the wheelhouse it
        compiles wheels and then runs again. """
        pip_inst = ("{}/bin/pip install --no-index --use-wheel --find-links='{}'"
                    " --download-cache='{}' {}"
                    .format(self.venv_dir, self.wheeldir, self.cachedir, pip_fragment))
        # If error (non zero ret), assume that there weren't valid wheels
        if self.system(pip_inst):
            self.req("{}/bin/pip wheel --download-cache='{}' --wheel-dir='{}' {}"
                     .format(self.venv_dir, self.cachedir, self.wheeldir, pip_fragment))

        # Try to install now with valid wheels
        self.req(pip_inst)

    def current_rev(self):
        self.githash = self.system(
            "git --git-dir {repo_dir}/.git rev-parse {rev}"
            .format(**self.__dict__), output=True)
        assert len(self.githash) == 40
        venv_name = self.system(self.venv_name_command.format(**self.__dict__), output=True)[:30].rstrip("-")
        venv_name += "-{}".format(self.githash)
        self.logger.info("Parsed githash for repository {}".format(self.githash))

        # If not provided, use basedir
        if self.venv_dir is None:
            self.venv_dir = os.path.join(self.basedir, venv_name)
        # If provided but relative, join to basedir
        elif not os.path.isabs(self.venv_dir):
            self.venv_dir = os.path.realpath(os.path.join(self.basedir, self.venv_dir, venv_name))
        # If absolute, join to given abs path
        else:
            self.venv_dir = os.path.join(self.venv_dir, venv_name)

    def create(self):
        """ Creates a virtualenv for a specific python package """
        self.current_rev()
        if os.path.isdir(self.venv_dir):
            self.fail("venv dir {} already exists! Aborting.".format(self.venv_dir))

        self.logger.info(self.color("Marking sha hash in repository", self.HEADER))
        repo = os.path.join(self.repo_dir, self.package)
        if self.tag:
            self.req(r'echo "__sha__ = \"{}\"" >> {}/__init__.py'.format(self.githash, repo))
        self.req("virtualenv {}".format(self.venv_dir))
        self.req("{}/bin/pip install wheel".format(self.venv_dir))
        self.try_pip("-r {}".format(os.path.join(self.repo_dir, "requirements.txt")))
        for extra in self.extra_requirements:
            self.try_pip("-r {}".format(extra))
        self.req("{}/bin/pip install {}".format(self.venv_dir, self.repo_dir))
        if self.tag:
            self.req("git --git-dir {0}/.git --work-tree {0} checkout -- {1}/__init__.py"
                     .format(self.repo_dir, self.package))
        self.logger.info(self.color("#### SUCCESS ####", self.OKGREEN))

    def is_venv(self, folder):
        dirs = set(os.walk(folder).next()[1])
        return set(["bin", "include", "lib", "local"]).issubset(dirs)

    def num_links(self, f):
        self.req("stat -c '%h' {}".format(f))

    def find_venvs(self):
        for folder in os.walk(self.basedir).next()[1]:
            if self.is_venv(folder):
                seconds_since_create = int(time.time() - os.stat(folder).st_ctime)
                age = datetime.timedelta(seconds=seconds_since_create)
                links = os.stat(os.path.join(folder, "bin", self.executable)).st_nlink - 1
                yield age, links, folder

    def clean_venvs(self):
        for age, links, folder in self.find_venvs():
            if links == 0:
                print("Found venv {}, age {}, with no links to the binary."
                      .format(folder, age))
                if raw_input("Would you like to delete it? [y/n]") == "y":
                    self.req("rm -rf {}".format(folder))
            else:
                print("Found venv {}, age {}, with {} links. Ignoring."
                      .format(folder, age, links))

    def list_venvs(self):
        print("Age\tLinks\tName")
        for vals in self.find_venvs():
            print("{}\t{}\t{}".format(*vals))

    def link(self, rev=None):
        if rev is None:
            self.current_rev()

        for name in self.names:
            self.logger.info("Linking {} to {}".format(name, self.venv_dir))
            self.req("ln --no-dereference -f {}/bin/{} {}"
                     .format(self.venv_dir, self.executable, name))


def main():
    parser = argparse.ArgumentParser(prog='venv deploy')
    parser.add_argument('-l', '--log-level', default="INFO",
                        choices=['DEBUG', 'INFO', 'WARN', 'ERROR'])
    parser.add_argument('-c', '--config', default="deploy.json")
    subparsers = parser.add_subparsers(title='main subcommands', dest='action')

    subparsers.add_parser('list_venvs')
    subparsers.add_parser('clean_venvs')
    create = subparsers.add_parser('create')
    create.add_argument('-r', '--rev', default="HEAD")
    link = subparsers.add_parser('link', help='links a list of executable names to the current git revision')
    link.add_argument('names', help='names of the hardlinks you\'d like to create', action='append')
    link.add_argument('-r', '--rev', default="HEAD")
    args = parser.parse_args()

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s'))
    root = logging.getLogger()
    root.setLevel(getattr(logging, args.log_level))
    root.addHandler(handler)

    logger = logging.getLogger("deploy")

    dep = Deploy(logger=logger, **vars(args))
    getattr(dep, args.action)()

if __name__ == "__main__":
    main()
