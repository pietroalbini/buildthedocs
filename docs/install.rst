.. _install:

~~~~~~~~~~~~~~~~~~~~~~~
Installing BuildTheDocs
~~~~~~~~~~~~~~~~~~~~~~~

BuildTheDocs is publicly available on PyPI, so the installation process is
fast and straightforward. Here you can also learn how to build it from source.

.. _install-deps:

===================
System dependencies
===================

In order to provide a reliable git_ support, BuildTheDocs needs the libgit2,
libffi and libssh2 system libraries to be present in the host. Also, if you
want to speed up YAML files parsing, you may want to install also the
libyaml system library. And because it needs C extensions, python headers are
also required.

On Debian/Ubuntu systems, you can install those with the following command::

   $ apt-get install libgit2-dev libffi-dev libssh2-1-dev libyaml-dev python3-dev

Please remember that pygit2 - a dependency of BuildTheDocs - must be the
**exact** same version of libgit2, otherwise it won't compile. On
Debian/Ubuntu you can check the version of the libgit2 library with the
following command::

   $ apt-cache show libgit2-dev

.. _install-pip:

===========================
Installing via PyPI and pip
===========================

As said before, BuildTheDocs is available on PyPI, so it can be installed with
only the following command (assuming you've pip_ installed)::

   $ pip install buildthedocs

.. _install-source:

====================
Building from source
====================

If you want to build BuildTheDocs from source, for example if you have changed
the source code or if you don't trust the package, first you need to obtain
the source::

   $ git clone https://github.com/pietroalbini/buildthedocs

Then, you can build and install it with the ``setup.py`` script::

   $ cd buildthedocs
   $ python3 setup.py install

.. _git: http://git-scm.com
.. _pip: https://pip.pypa.io
