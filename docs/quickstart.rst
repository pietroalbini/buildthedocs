.. _quickstart:

~~~~~~~~~~~~~~~~~~~~~~~~
Start using BuildTheDocs
~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial will teach you how to configure and build your first project
with BuildTheDocs. It assumes you've installed the tool, otherwise follow
the :ref:`install` charapter first.

In this tutorial we'll build this documentation both for the latest version
and the development branch.

.. _quickstart-config:

================================
Creating the configuration files
================================

In order to build a project, BuildTheDocs needs to know some piece of
information about it. These information are provided by a YAML-formatted
configuration file.

Here there is the configuration file for the project we want to build::

   versions:
     - name: "dev"
       source:
         provider: git
         url: https://github.com/pietroalbini/buildthedocs.git
         checkout: master
       directory: docs
       title: Development
       notice: unstable
       warning: This documentation is for the in-development and unstable version of BuildTheDocs!

     - name: "1.0"
       source:
         provider: git
         url: https://github.com/pietroalbini/buildthedocs.git
         checkout: "1.0"
       directory: docs
       title: BuildTheDocs 1.0
       notice: null
       warning: null

So, let's see what this configuration file does: in the ``versions`` section
we start defining all the versions we want to build. Each version has a name,
the pieces of information about how to get the source, the directory in which
the documentation is, and some pieces of information in order to compose the
version chooser in a better way.

You can learn more about this in :ref:`config` charapter of the documentation.

.. _quickstart-build:

====================================
Building from the configuration file
====================================

Then, you need to actually build the project, so you can run the following
command, assuming the configuration file is located in ``config.yml``::

   $ buildthedocs config.yml

That command will build all versions present in that configuration file, and
place the output in the ``build`` directory. If you want to build only some
versions or change the output directory, you can do so::

   $ buildthedocs -o output/ config.yml 1.0 dev

==========
Growing up
==========

Congrats, you've builded your first documentation with BuildTheDocs! Now, if
you want to know more about it, you should explore the documentation a bit
further.

Here are some topics you may want to know:

* :ref:`scripting`
* :ref:`source-providers-custom`
