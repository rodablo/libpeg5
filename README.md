# _THIS IS A WORK IN PROGRESS_

To be completed.

Dependencies
============

To use/compile libpe5lang you will need:

* Python 3.? (or newer).
* A recent version of the GNAT Ada compiler, either from your OS's packages, or from [here](https://www.adacore.com/download).
* Langkit (https://github.com/AdaCore/langkit.git).


Build
=====

Get the source code and optionally create a python virtual environment.

```sh
git clone https://github.com/rodablo/libpeg5.git
cd libpeg5
python3 -m venv venv
source ./venv/bin/activate
cd -
```

Get and install last version of e3-testsuite

```sh
pip install wheel
git clone https://github.com/AdaCore/e3-testsuite.git
cd ~/e3-testsuite
pip install .
cd -
```

Get and install Langkit

```sh
git clone https://github.com/AdaCore/langkit.git
cd ~/langkit
pip install .
cd -
```

Follow the install instructions for langkit-support

Build libpeg5

```sh
./manage.py make -b dev
```

...

```sh
eval $(./manage.py setenv)
./manage.py test
```

Peg5
====

Some [peg description](./peg5/language/README.md)