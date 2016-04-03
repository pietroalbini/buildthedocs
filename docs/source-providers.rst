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

.. _name of the compression algorithm: https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats
