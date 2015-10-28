pybolator
=========

PyBoard emulator

Dependencies
------------

python3-tk
``````````
Debian based distros::

  $ apt-get install python3-tk

Run
---
::

  $ PYBOLATOR_MAIN=path/to/your/main.py python3 pybolator.py

Development
-----------
::

  $ mkvirtualenv --python=/path/to/python3.x pybolator
  $ workon pybolator
  $ PYBOLATOR_MAIN=test.py python pybolator.py
