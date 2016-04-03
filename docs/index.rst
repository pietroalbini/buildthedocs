.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _index:

==========================
BuildTheDocs documentation
==========================

*A Sphinx documentation building tool on steroids.*

BuildTheDocs is a tool which helps building Sphinx_ documentation, for multiple
releases of a project. It builds all the releases' docs with only one command
while customizing them, for example adding a simple release chooser.

BuildTheDocs also provides a simple API to hook into the build project, so you
can add dynamic parts of the documentation at runtime. An example of this
integration is the release chooser. You can also hack it as you want because
it's released under the MIT license.

.. _index-introduction:

Introduction to BuildTheDocs
============================

.. toctree::
   :maxdepth: 2

   install
   quickstart

.. _index-narrative:

Narrative documentation
=======================

.. toctree::
   :maxdepth: 3

   config
   source-providers
   scripting
   customize/index

.. _index-reference:

Reference
=========

.. toctree::
   :maxdepth: 2

   cli
   api

.. _index-sidenotes:

Side notes
==========

.. toctree::
   :maxdepth: 2

   changelog
   license

.. _Sphinx: http://sphinx-doc.org
