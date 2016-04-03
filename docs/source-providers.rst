.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _source-providers:

================
Source providers
================

Source providers are the way to fetch your project's source code while building
your documentation. There are some useful ones bundled with BuildTheDocs, but
you can also create your own ones!

.. _source-providers-local:

The local provider
==================

The local provider is the simplest one available, which simply takes a
directory from the local filesystem and copy that to the output destination.

It requires the ``path`` key, which should contain the path where the source
is located.

.. code-block:: plain

   source:
     provider: local
     path: /home/john/docs

.. _source-providers-url:

The url provider
================

The url provider downloads a compressed archive from the Internet, and then it
extracts it to the output destination.

It requires the ``url`` key, which should contain the url to the file, and the
``compression`` key, which must contain the `name of the compression
algorithm`_ used by the archive.

.. code-block:: plain

   source:
     provider: url
     path: http://www.example.com/download/docs.tar.gz
     compression: gztar

.. _source-providers-git:

The git provider
================

The git provider clones a git repository to the output destination, and
switches to the branch you want to build the documentation from.

It requires the ``url`` key, which should contains the url to the git repo,
and the ``checkout`` key, which should contains the branch you want to
checkout to.

.. code-block:: plain

   source:
     provider: git
     url: git@git.example.com:repository.git
     checkout: master

.. _source-providers-custom:

Creating your own source provider
=================================

If you need to get the source code of your documentation from a souce which
hasn't a source provider by default, you can easily create that.

A source provider is any callable Python object, which must accept two
arguments: the version configuration and the destination of the source code.
For the current example, we're going to replicate the ``local`` builtin source
provider:

.. code-block:: python

   import shutil

   def my_provider(config, dest):
       # shutil.copytree copies a directory
       shutil.copytree(config["source"]["path"], dest)

Then you can start using it. Remember that you can use custom providers only
when building from a script, making an instance of the builder (it's explained
how to do so in the ":ref:`scripting-custom`" section of the documentation),
as so:

.. code-block:: python

   import yaml
   import buildthedocs

   with open("config.yml") as f:
      config = yaml.load(f.read())

   builder = buildthedocs.Builder(config, "build/")
   builder.register_source_provider("custom", my_provider)
   builder.build()

That snippet will register the provider we wrote before under the ``custom``
name, and we can now use it in the configuration file:

.. code-block:: plain

   source:
     provider: custom
     path: /home/john/docs

.. _name of the compression algorithm: https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats
