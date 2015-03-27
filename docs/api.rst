~~~~~~~~~~~~~
API reference
~~~~~~~~~~~~~

There you can find the documentation for the API BuildTheDocs exposes.

.. py:module:: buildthedocs

==============
High level API
==============

The high-level API can be used if you want to use BuildTheDocs without any
special need. It doesn't provide too much customization capabilities.

.. py:function:: build(config, [*versions, output="build"])

   Execute the build process as if it was done thorught the commad line. It
   accepts as ``config`` both a YAML file path or a dict. You may specify
   which versions to build passing them as arguments, but if you don't provide
   any of these all versions will be builded. You can also customize which
   output directory you want to use.

=============
Low level API
=============

The low-level API is a little bit more advanced to be used, but it provides
full customization support.

.. py:class:: Builder(config, output)

   The Builder class is the one which configures new builder processes. If you
   want to have better control of the build, you should use this.

   It requires a dict containing the configuration, and an output directory.
   It doesn't also automatically parse YAML files, you should do that by
   yourself.

   .. py:method:: register_source_provider(name, provider)

      Register a new source provider, as explained in the
      ":ref:`source-providers-custom`" charapter of the documentation.

      It requires the name of the provider and the callable provider.
      It raises a ``NameError`` if a provider with the same name was already
      registered.

   .. py:method:: build(*versions)

      Execute a build of the passed versions. If you don't provide any version
      all the existing versions will be builded. You can call this method all
      the times you want.

.. py:class:: BuildProcess(builder, version, details)

   This class implements the actual documentation building process, so if you
   want to hook into it you should subclass this class. To actually customize
   the build behavior, you should read the class source code, and extend the
   build private methods.

   It requires the builder instance, the version codename and the
   configuration details.

   .. py:method:: execute

      This method starts the build process and it will call all methods needed
      for the build. Hook here only if you want to add custom methods.
