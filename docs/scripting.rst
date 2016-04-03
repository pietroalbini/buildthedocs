.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _scripting:

==================================
Calling BuildTheDocs from a script
==================================

If you're writing a Python script which needs to execute BuildTheDocs, you can
directly call the Python API instead of executing the CLI command.

Direct calls to the Python API are way faster than the corresponding calls to
the command line tool, since the operative system needs to spawn a new
process and a new Python interpreter in the latter case. Also, the Python API
allows you to customize your build beyond the defaults.

.. _scripting-base:

Executing a basic build
=======================

Executing a build without customizing it is really straightforward:

.. code-block:: python

   import buildthedocs
   buildthedocs.build("config.yml")

These two lines of code are equivalent to::

   $ buildthedocs config.yml

As the command line tool, you can specify which versions you want to build,
and also the output directory:

.. code-block:: python

   import buildthedocs
   buildthedocs.build("config.yml", "1.0", "1.1", output="../docs")

.. _scripting-custom:

Using a custom builder
======================

If you want to have more control on the process, or you want to customize it,
creating a custom builder instance is the way to go:

.. code-block:: python

   import yaml
   import buildthedocs

   with open("config.yml") as f:
       config = yaml.load(f.read())

   builder = buildthedocs.Builder(config, "build/")
   builder.build()

The initializator of the class requires the configuration as a dict and the
output directory, and you can provide to the build method the versions you
want to build. You can also call the build method as many times you want.

If you want to load the config from a file, you need to manually parse it. The
example parses a YAML file.
