.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _install:

=======================
Installing BuildTheDocs
=======================

BuildTheDocs is publicly available on PyPI, so the installation process is
fast and straightforward. Here you can also learn how to build it from source.

.. _install-pip:

Installing via PyPI and pip
===========================

As said before, BuildTheDocs is available on PyPI, so it can be installed with
only the following command (assuming you've pip_ installed)::

   $ python3 -m pip install buildthedocs

If you don't have root privileges on your account and the previous command
fails because of that, you can wrap the command with ``sudo`` to execute it::

   $ sudo python3 -m pip install buildthedocs

.. _install-source:

Building from source
====================

If you want to build BuildTheDocs from source, for example if you have changed
the source code or if you don't trust the package, first you need to obtain
the source::

   $ git clone https://github.com/pietroalbini/buildthedocs

Then, you can build and install it with pip_::

   $ cd buildthedocs
   $ python3 -m pip install .

.. _pip: https://pip.pypa.io
