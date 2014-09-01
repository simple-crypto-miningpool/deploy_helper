deploy
======

A basic virtualenv creation utility

This is just a tool I made for myself, so documentation is basically non-existent... Here's how it's used tho.

````
$ deploy_helper create                                                
2014-09-01 16:07:33,919 [INFO]: -- git --git-dir /home/isaac/programming/powerpool/.git --no-pager log -1 --format='%f-%H' HEAD
2014-09-01 16:07:33,924 [INFO]: -- git --git-dir /home/isaac/programming/powerpool/.git rev-parse HEAD
2014-09-01 16:07:33,928 [INFO]: Parsed githash for repository eb60db151066a7bd858a95e96f8993dd1283266f
2014-09-01 16:07:33,929 [INFO]: Marking sha hash in repository
2014-09-01 16:07:33,930 [INFO]: -- echo "__sha__ = \"eb60db151066a7bd858a95e96f8993dd1283266f\"" >> /home/isaac/programming/powerpool/powerpool/__init__.py
2014-09-01 16:07:33,931 [INFO]: -- virtualenv /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f
New python executable in /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin/python
Installing setuptools, pip...done.
2014-09-01 16:07:35,288 [INFO]: -- /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin/pip install wheel
Downloading/unpacking wheel
  Downloading wheel-0.24.0-py2.py3-none-any.whl (63kB): 63kB downloaded
Installing collected packages: wheel
Successfully installed wheel
Cleaning up...
2014-09-01 16:07:36,116 [INFO]: -- /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin/pip install --no-index --use-wheel --find-links='/home/isaac/programming/deploy/test/wheelhouse' --download-cache='/home/isaac/programming/deploy/test/pipcache' -r /home/isaac/programming/powerpool/requirements.txt
Ignoring indexes: https://pypi.python.org/simple/
Downloading/unpacking cryptokit from git+https://github.com/simplecrypto/cryptokit.git@v0.2.10 (from -r /home/isaac/programming/powerpool/requirements.txt (line 2))
  Cloning https://github.com/simplecrypto/cryptokit.git (to v0.2.10) to ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/build/cryptokit
  Running setup.py (path:/home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/build/cryptokit/setup.py) egg_info for package cryptokit
    
Downloading/unpacking gevent==1.0.1 (from -r /home/isaac/programming/powerpool/requirements.txt (line 3))
Downloading/unpacking PyYAML==3.10 (from -r /home/isaac/programming/powerpool/requirements.txt (line 4))
Downloading/unpacking Flask==0.10.1 (from -r /home/isaac/programming/powerpool/requirements.txt (line 5))
Downloading/unpacking setproctitle==1.1.8 (from -r /home/isaac/programming/powerpool/requirements.txt (line 6))
Downloading/unpacking Jinja2==2.7.3 (from -r /home/isaac/programming/powerpool/requirements.txt (line 9))
Downloading/unpacking MarkupSafe==0.23 (from -r /home/isaac/programming/powerpool/requirements.txt (line 10))
Downloading/unpacking Werkzeug==0.9.6 (from -r /home/isaac/programming/powerpool/requirements.txt (line 11))
Requirement already satisfied (use --upgrade to upgrade): argparse==1.2.1 in /usr/lib/python2.7 (from -r /home/isaac/programming/powerpool/requirements.txt (line 12))
Downloading/unpacking future==0.11.2 (from -r /home/isaac/programming/powerpool/requirements.txt (line 13))
Downloading/unpacking greenlet==0.4.3 (from -r /home/isaac/programming/powerpool/requirements.txt (line 14))
Downloading/unpacking itsdangerous==0.24 (from -r /home/isaac/programming/powerpool/requirements.txt (line 15))
Requirement already satisfied (use --upgrade to upgrade): wsgiref==0.1.2 in /usr/lib/python2.7 (from -r /home/isaac/programming/powerpool/requirements.txt (line 16))
Downloading/unpacking urllib3==1.9 (from cryptokit->-r /home/isaac/programming/powerpool/requirements.txt (line 2))
Installing collected packages: cryptokit, gevent, PyYAML, Flask, setproctitle, Jinja2, MarkupSafe, Werkzeug, future, greenlet, itsdangerous, urllib3
  Running setup.py install for cryptokit
    
Successfully installed cryptokit gevent PyYAML Flask setproctitle Jinja2 MarkupSafe Werkzeug future greenlet itsdangerous urllib3
Cleaning up...
2014-09-01 16:07:38,695 [INFO]: -- /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin/pip install --no-index --use-wheel --find-links='/home/isaac/programming/deploy/test/wheelhouse' --download-cache='/home/isaac/programming/deploy/test/pipcache' -r /home/isaac/programming/powerpool/requirements.txt
Ignoring indexes: https://pypi.python.org/simple/
Requirement already satisfied (use --upgrade to upgrade): cryptokit from git+https://github.com/simplecrypto/cryptokit.git@v0.2.10 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 2))
Requirement already satisfied (use --upgrade to upgrade): gevent==1.0.1 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 3))
Requirement already satisfied (use --upgrade to upgrade): PyYAML==3.10 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 4))
Requirement already satisfied (use --upgrade to upgrade): Flask==0.10.1 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 5))
Requirement already satisfied (use --upgrade to upgrade): setproctitle==1.1.8 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 6))
Requirement already satisfied (use --upgrade to upgrade): Jinja2==2.7.3 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 9))
Requirement already satisfied (use --upgrade to upgrade): MarkupSafe==0.23 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 10))
Requirement already satisfied (use --upgrade to upgrade): Werkzeug==0.9.6 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 11))
Requirement already satisfied (use --upgrade to upgrade): argparse==1.2.1 in /usr/lib/python2.7 (from -r /home/isaac/programming/powerpool/requirements.txt (line 12))
Requirement already satisfied (use --upgrade to upgrade): future==0.11.2 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 13))
Requirement already satisfied (use --upgrade to upgrade): greenlet==0.4.3 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 14))
Requirement already satisfied (use --upgrade to upgrade): itsdangerous==0.24 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from -r /home/isaac/programming/powerpool/requirements.txt (line 15))
Requirement already satisfied (use --upgrade to upgrade): wsgiref==0.1.2 in /usr/lib/python2.7 (from -r /home/isaac/programming/powerpool/requirements.txt (line 16))
Requirement already satisfied (use --upgrade to upgrade): urllib3==1.9 in ./Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/lib/python2.7/site-packages (from cryptokit->-r /home/isaac/programming/powerpool/requirements.txt (line 2))
Cleaning up...
2014-09-01 16:07:38,905 [INFO]: -- /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin/pip install /home/isaac/programming/powerpool
Unpacking /home/isaac/programming/powerpool
  Running setup.py (path:/tmp/pip-cGZiG2-build/setup.py) egg_info for package from file:///home/isaac/programming/powerpool
    
Installing collected packages: powerpool
  Running setup.py install for powerpool
    
    Installing pp script to /home/isaac/programming/deploy/test/Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f/bin
Successfully installed powerpool
Cleaning up...
2014-09-01 16:07:39,610 [INFO]: -- git --git-dir /home/isaac/programming/powerpool/.git --work-tree /home/isaac/programming/powerpool checkout -- powerpool/__init__.py
2014-09-01 16:07:39,617 [INFO]: #### SUCCESS ####


$ deploy_helper list_venvs
Age	Links	Name
0:25:48	1	Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f

$ deploy_helper link -r HEAD~1 test                                                                                                                                                                                              20 ↵
2014-09-01 16:04:31,181 [INFO]: -- git --git-dir /home/isaac/programming/powerpool/.git --no-pager log -1 --format='%f-%H' HEAD~1
2014-09-01 16:04:31,184 [INFO]: -- git --git-dir /home/isaac/programming/powerpool/.git rev-parse HEAD~1
2014-09-01 16:04:31,190 [INFO]: Parsed githash for repository 643bdd8dd72c64bc9011f70bf1a491befc3d6d77
2014-09-01 16:04:31,190 [INFO]: Linking test to /home/isaac/programming/deploy/test/Add-component-oriented-client-views-643bdd8dd72c64bc9011f70bf1a491befc3d6d77
2014-09-01 16:04:31,190 [INFO]: -- ln --no-dereference -f /home/isaac/programming/deploy/test/Add-component-oriented-client-views-643bdd8dd72c64bc9011f70bf1a491befc3d6d77/bin/pp test

$ deploy_helper clean_venvs                  
Found venv Add-component-oriented-client-views-643bdd8dd72c64bc9011f70bf1a491befc3d6d77, age 0:06:08, with no links to the binary.
Would you like to delete it? [y/n]y
2014-09-01 16:05:52,502 [INFO]: -- rm -rf Add-component-oriented-client-views-643bdd8dd72c64bc9011f70bf1a491befc3d6d77
Found venv Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f, age 0:40:30, with no links to the binary.
Would you like to delete it? [y/n]y
2014-09-01 16:05:54,520 [INFO]: -- rm -rf Fix-broken-main-stats-view-eb60db151066a7bd858a95e96f8993dd1283266f
````
