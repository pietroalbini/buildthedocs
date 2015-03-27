.. _cli:

~~~~~~~~~~~~~~~~~~~~~~~~~~
The command line interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

The BuildTheDocs command line interface is the ``buildthedocs`` command, which
allows you to build things without calling the Python API directly.

It has the following definition::

   $ buildthedocs [-h] [-o OUTPUT_DIR] CONFIG_FILE [VERSION [VERSION ...]]

It always requires a valid path to a configuration file, and optionally the
versions you want to build. It also supports the following options:

.. option:: -h, --help

   Show the help for the command.

.. option:: -o OUTPUT_DIR, --output OUTPUT_DIR

   Change the output directory, the default is ``build/``.
