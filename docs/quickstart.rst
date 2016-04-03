.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _quickstart:

========================
Start using BuildTheDocs
========================

Now that you've :ref:`installed <install>` BuildTheDocs, it's time to build
your first project with it. In this tutorial we're going to build the master
branch of BuildTheDocs and the ``1.0`` release of it.

.. _quickstart-config:

Creating the configuration files
================================

In order to build a project, BuildTheDocs needs to know some piece of
information about it. These information are provided by a YAML-formatted
configuration file.

Open your favourite text editor and put this content in it:

.. code-block:: plain

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

Let's analyze this configuration file:

* Every version we want to build is defined as an item in the top-level
  ``versions`` list.

* Every version has a codename in the ``name`` key, which will be used in the
  docs' URL.

* The :ref:`information needed <source-providers>` to fetch the source code is
  in the ``source`` key.

* If the documentation isn't in the root of the fetched source code, you can
  define the directory in which it is with the ``directory`` key.

* You can customize the entry of this version in the version chooser with the
  ``title`` (required) and the ``notice`` (can be ``null``) keys.

* You can also put a warning in the top of the documentation with the
  ``warning`` key.

If you want to learn more about how configuration files works, check out the
:ref:`chapter about configuration files <config>`.

.. _quickstart-build:

Building from the configuration file
====================================

Now that you've written the configuration file, you can actually build the
project. In order to do that, you can run the following command, assuming the
configuration file is located in ``config.yml``::

   $ buildthedocs config.yml

That command will build all versions you defined, and place the output in the
``build`` directory. If you want to build only some versions or change the
output directory, you can easily do so::

   $ buildthedocs -o output/ config.yml 1.0 dev

.. _quickstart-growing-up:

Growing up
==========

Congrats, you've builded your first documentation with BuildTheDocs! Now, if
you want to know more about it, you should explore the documentation a bit
further.

Here are some topics you may want to know:

* :ref:`scripting`
* :ref:`customize`
