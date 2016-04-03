.. Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
   Released under the CC-BY 4.0 International license

.. _api:

=============
API reference
=============

Here you can find the documentation for the public API BuildTheDocs exposes.
This API will be kept backwards compatible until the next major release, but
existing features might be deprecated.

.. _api-high:

High level API
==============

The high-level API can be used if you want to use BuildTheDocs without any
custom customization. It allows you to use only the default customizations
shipped with BuildTheDocs itself.

.. py:function:: buildthedocs.build(config, [*versions, output="build"])

   Execute the build process as if it was done thorught the commad line. It
   accepts as ``config`` both a YAML file path or a dict. You may specify
   which versions to build passing them as arguments, but if you don't provide
   any of these all versions will be builded. You can also customize which
   output directory you want to use.

   :param str config: Path to the YAML configuration file
   :param str \*versions: All the versions you want to build (everyone if
                          omitted)
   :param str build: The output directory (default ``build/``)

.. _api-low:

Low level API
=============

The low-level API is a little bit more verbose and advanced to be used, but it
allows you to customize the build as you want, without any limitation.

.. py:class:: buildthedocs.Builder(config, output)

   The Builder class is the one which configures new builder processes. If you
   want to have better control of the build, you should use this.

   It requires a dict containing the configuration, and an output directory.
   It doesn't also automatically parse YAML files, you should do that by
   yourself.

   :param dict config: The build configuration (already parsed)
   :param str output: The output directory

   .. py:method:: register_source_provider(name, provider)

      Register a new source provider, as explained in the
      ":ref:`source-providers-custom`" charapter of the documentation.

      It requires the name of the provider and the callable provider.
      It raises a ``NameError`` if a provider with the same name was already
      registered.

      :param str name: The name of the source provider
      :param callable provider: The provider you want to register

   .. py:method:: build(\*versions)

      Execute a build of the passed versions. If you don't provide any version
      all the existing versions will be builded. You can call this method all
      the times you want.

      :param str \*versions: The versions you want to build (everyone if
                             omitted)

.. py:class:: buildthedocs.BuildProcess(builder, version, details)

   This class implements the actual documentation building process, so if you
   want to hook into it you should subclass this class. To actually customize
   the build behavior, you should read the class source code, and extend the
   build private methods.

   :param buildthedocs.Builder builder: The builder instance
   :param str version: The version you want to build
   :param dict details: The configuration for this specific version

   .. py:method:: execute()

      This method starts the build process and it will call all methods needed
      for the build. Hook here only if you want to add custom methods.
