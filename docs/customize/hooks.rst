.. Copyright (c) 2016 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _customize-hooks:

=================
Add a custom hook
=================

Hooks allows you to change your documentation without building it. For example,
you can add a custom sidebar with dynamic content or replace the search bar to
point to your own search engine.

.. versionadded:: 1.1

.. _customize-hooks-capabilities:

What you can do with hooks
==========================

Hooks are able to dynamically add and change your documentation's source code.
Other than the common things you can do with simple file system access,
BuildTheDocs allows you to do some higher-level operations.

.. _customize-hooks-capabilities-templates:

Custom templates
----------------

You can add custom templates by providing the HTML source of them to the
:py:meth:`~buildthedocs.BuildProcess.add_template` method of the ``process``.
For example, you can extend the default layout to add the build date to the
footer:

.. code-block:: python

   import datetime

   TEMPLATE = """
   {% extends "!layout.html" %}
   {% block footer %}
       {{ super() }}
       <p>Last build at ##time##</b>
   {% endblock %}
   """

   def build_time_hook(builder, process):
       now = datetime.datetime.now()
       tmpl = TEMPLATE.replace("##time##", str(now))

       process.add_template("layout", tmpl)

.. _customize-hooks-capabilities-sidebars:

Custom sidebars
---------------

The sidebar is one of the best place to put utility content: it doesn't
distract the reader but it's easily accessible.

Adding some content to the sidebar is really simple! You just need to provide
the source code of the box you want to add to the
:py:meth:`~buildthedocs.BuildProcess.add_sidebar` method of the ``process``.
For example, you can add the build date on the sidebar with this code:

.. code-block:: python

   import daetime

   def build_time_hook(builder, process):
       now = datetime.datetime.now()
       process.add_sidebar("<p>"+str(now)+"</p>")

.. _customize-hooks-capabilities-objects:

Access build objects
--------------------

BuildTheDocs stores a lot of useful state information in the
:py:class:`~buildthedocs.Builder` and :py:class:`~buildthedocs.BuildProcess`
instances, and you can easily access them.

For example, you can add a warning if you're not using the latest release, or
access some custom keys in the configuration files. Check out their API
documentation to see everything you can do with them!

.. _customize-hooks-create:

Create an hook
==============

Creating an hook is really easy. You need to create a callable Python object
(for example a function) which accepts an instance of the current
:py:class:`~buildthedocs.Builder` and :py:class:`~buildthedocs.BuildProcess`.

As an example, we're going to add a sidebar with some credits in it.

.. code-block:: python

   def credits_hook(builder, process):
       process.add_sidebar("<p>Built with BuildTheDocs.</p>")

.. _customize-hooks-register:

Register your hook
==================

Now it's time to add this to your build process. There are multiple ways to do
so: you can add it :ref:`to your distribution <distributions>`, add it globally
into one script or register it in a specific builder instance.

.. _customize-hooks-register-globally:

Register your hook globally
---------------------------

The easiest way to register your hook is to create a build script with the hook
in it. Then, with the :py:func:`buildthedocs.hook` decorator you can register
it globally in your script:

.. code-block:: python

   import buildthedocs

   @buildthedocs.hook
   def credits_hook(builder, process):
       process.add_sidebar("<p>Built with BuildTheDocs.</p>")

   buildthedocs.build("config.yml")

.. _customize-hooks-register-builder:

Register your hook in a Builder instance
----------------------------------------

If you don't like to mess up with global state or you need to do multiple
builds with different hooks, you can add your hook directly into the
:py:class:`~buildthedocs.Builder` instance, with the
:py:meth:`~buildthedocs.Builder.register_hook` method:

.. code-block:: python

   import buildthedocs

   def credits_hook(builder, process):
       process.add_sidebar("<p>Built with BuildTheDocs.</p>")

   with open("config.yml") as f:
       config = yaml.load(f.read())

   builder = buildthedocs.Builder(config, "build/")
   builder.register_hook(credits_hook)
   builder.build()
