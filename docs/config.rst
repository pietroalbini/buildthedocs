.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _config:

=======================
The configuration files
=======================

BuildTheDocs needs to know what it should build and how, and the way to tell it
those information is to write a configuration file. BuildTheDocs' configuration
files are written in YAML, a simple, elegant and human-readable serialization
format.

.. _config-yaml:

YAML primers
============

YAML represents keys and values, grouped in dictionaries and lists. Each
key-value pair must be in its own line, and grouped in its parent with
indentation. Keys and values are separated with a ``:``, and quotes aren't
needed for strings (but are supported). Lists are marked with a ``-`` in front
of the key-value pair. It also supports comments.

For example, this is a valid YAML file:

.. code-block:: plain

   # Hey, that's a comment!

   name: John
   age: 27
   interests:
     - programming
     - hiking
   projects:
     foo:
       status: completed
     bar:
       status: in progress
       tasks:
         - name: complete the status bar
           priority: low
         - name: fix authentication
           priority: high

If you want to learn more, check out the official `YAML specification`_.

.. _config-anatomy:

Anatomy of a configuration file
===============================

As said before, the BuildTheDocs configuration files are YAML-formatted, so
they should end with ``.yml`` or ``.yaml``. They are made of two different
sections: a metadata part, which currently contains nothing, and an array of
versions you want to build.

.. code-block:: plain

   versions:

     - name: "dev"
       source:
         provider: local
         path: ~/projects/myproject/docs
       directory: .
       title: Development
       notice: unstable
       warning: This isn't released yet!

     - name: "1.0"
       source:
         provider: git
         url: https://git.example.com/myproject.git
         checkout: "1.0"
       directory: docs
       title: MyProject 1.0
       notice: null
       warning: null

.. _config-versions:

The versions section
====================

The versions part is a list of multiple version dicts.

A version dict is composed of these keys:

* **source** contains all informations about how to get the documentation
  source code

  * **provider** define which source provider you want to use
  * all the keys needed by that provider

* **directory** contains the directory in the source tree in which the docs
  are located
* **title** contains the title of the current version, used in the version
  chooser
* **notice** contains an optional notice appended to the version title, but
  rendered as small
* **warning** contains an optional warning which will be appear on top of all
  the documentation pages for that version

If optional parameters aren't present, set them to ``null``.

You can see which source providers are available and which keys they uses in
the :ref:`source-providers` charapter of the documentation.

.. _YAML specification: http://www.yaml.org/spec/1.2/spec.html
