.. Copyright (c) 2016 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _customize-source-providers:

============================
Add a custom source provider
============================

BuildTheDocs natively supports fetching source code in the most popular ways
(in the open-source community), but you might need a completly different way to
do that. Because of this, BuildTheDocs natively supports adding third-party
source providers.

.. _customize-source-providers-create:

Create the source provider
==========================

Creating them is really easy. You need to create a callable Python object (for
example a function) which accepts the version configuration and the destination
directory, and put with that function the source code in its destination.

As an example, this is the code to replicate the behavior of the default
``local`` provider:

.. code-block:: python

   import shutil

   def mylocal_provider(config, dest):
       # shutil.copytree copies a directory
       shutil.copytree(config["source"]["path"], dest)

.. _customize-source-providers-register:

Register your source provider
=============================

Now it's time to add this to your build process. There are multiple ways to do
so: you can add it :ref:`to your distribution <distributions>`, add it globally
into one script or register it in a specific builder instance.

.. _customize-source-providers-register-globally:

Register your source provider globally
--------------------------------------

The easiest way to register your source provider is to create a build script
with the provider in it. Then, with the :py:func:`buildthedocs.source_provider`
decorator you can register it globally in your script:

.. code-block:: python

   import buildthedocs
   import shutil

   @buildthedocs.source_provider("mylocal")
   def mylocal_provider(config, dest):
       # shutil.copytree copies a directory
       shutil.copytree(config["source"]["path"], dest)

   buildthedocs.build("config.yml")

.. versionadded:: 1.1

.. _customize-source-providers-register-builder:

Register your source provider in a Builder instance
---------------------------------------------------

If you don't like to mess up with global state or you need to do multiple builds
with different source providers, you can add a specific source provider
directly into the :py:class:`~buildthedocs.Builder` instance, with the
:py:meth:`~buildthedocs.Builder.register_source_provider` method:

.. code-block:: python

   import buildthedocs
   import shutil
   import yaml

   def mylocal_provider(config, dest):
       # shutil.copytree copies a directory
       shutil.copytree(config["source"]["path"], dest)

   with open("config.yml") as f:
       config = yaml.load(f.read())

   builder = buildthedocs.Builder(config, "build/")
   builder.register_source_provider("mylocal", mylocal_provider)
   builder.build()

.. _customize-source-providers-use:

Use your new source provider
============================

Now that you can use your own source provider in your builds, it's time to
start using it: in your configuration file, choose the versions you want to
fetch with it and replace their ``source`` key with this:

.. code-block:: plain

   source:
     provider: mylocal
     path: /path/to/docs
