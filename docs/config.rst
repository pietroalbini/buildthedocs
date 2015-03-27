.. _config:

~~~~~~~~~~~~~~~~~~~~~~~
The configuration files
~~~~~~~~~~~~~~~~~~~~~~~

Here is explained how to write configuration files and how them works.

.. _config-yaml:

============
YAML primers
============

BuildTheDocs configuration files are written in YAML, a simple, beautiful
serialization format. This section explains the basics of it.

YAML represents keys and values, grouped in dictionaries and lists. Each
key-value pair must be in its own line, and grouped in its parent with
indentation. Keys and values are separated with a ``:``, and quotes aren't
needed for strings (but are supported). Lists are marked with a ``-`` in front
of the key-value pair.

For example, this is a valid YAML file::

   name: John
   age: 27
   interests:
   - programming
   - climbing
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

If you want to learn more, you can read the official `YAML specification`_.

.. _config-anatomy:

===============================
Anatomy of a configuration file
===============================

As said before, the BuildTheDocs configuration files are YAML-formatted, so
they should end with ``.yml`` or ``.yaml``.

They are composed by two different sections: a metadata part, which actually
contains nothing, and an array of versions you want to build.

If you don't want to write the file from scratch, you can customize the
configuration file in the :ref:`quickstart-config` section of the
documentation.

.. _config-versions:

====================
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
