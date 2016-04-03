.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _cli:

==========================
The command line interface
==========================

BuildTheDocs provides a command line interface, which allows you to build your
documentation without calling the Python API directly. You can interact with it
with the ``buildthedocs`` command. It has the following definition::

   $ buildthedocs [-h] [-o OUTPUT_DIR] CONFIG_FILE [VERSION [VERSION ...]]

It always requires a valid path to a configuration file, and optionally the
various versions you want to build. It also supports the following options:

.. option:: -h, --help

   Show the help for the command.

.. option:: -o OUTPUT_DIR, --output OUTPUT_DIR

   Change the output directory, the default is ``build/``.
