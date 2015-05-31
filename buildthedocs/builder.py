"""
    buildthedocs.builder
    Logic of the documentation builder

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import subprocess
import shutil
import os
import json

import yaml
import sphinx.application
import pygit2
import pkg_resources
import jinja2

import buildthedocs
from buildthedocs import utils


class BuildError(Exception):
    """ Error occured during a build """


class Builder:
    """ Instance of a builder """

    def __init__(self, config, output_to, only_inits=None, initializer=None):
        self.versions = {version["name"]: version
                         for version in config["versions"]}
        self.ordered_versions = config["versions"]

        self._output_to = output_to
        self._source_providers = {}
        self._hooks = []

        # If no initializator is provided, use the global one
        if initializer is None:
            initializer = buildthedocs._collector

        # Apply all the wanted initializators to this object
        initializer.apply(self, only_inits)

    def register_source_provider(self, name, provider):
        """ Register a new source provider """
        # Do some validation
        if name in self._source_providers:
            raise NameError('A source provider with the name "{}" already '
                            'exists'.format(name))
        if not callable(provider):
            raise ValueError('The provider must be callable')

        self._source_providers[name] = provider

    def register_hook(self, hook):
        """ Register a new hook """
        if not callable(hook):
            raise ValueError('The provider must be callable')

        self._hooks.append(hook)

    def build(self, version=None):
        """ Build a specific version """
        # If no version was provided build all the versions
        if version is None:
            results = []
            for version in self.versions:
                results.append(self.build(version))
            return results

        # Prevent non-existing versions
        if version not in self.versions:
            raise ValueError("Version {} doesn't exist".format(version))

        process = BuildProcess(self, version, self.versions[version])
        process.execute()

        return process.output_dir


class BuildProcess:
    """ A build process """

    def __init__(self, builder, version, config):
        self.config = config
        self.builder = builder
        self.version = version

        if "directory" in config:
            extra_source = config["directory"]
        else:
            extra_source = ""

        # Define some directory names
        self.output_dir = os.path.join(builder._output_to, version)
        self.btd_dir = os.path.join(self.output_dir, "__btd__")
        self.source_dir = os.path.join(self.btd_dir, "source", extra_source)

        self._sidebars = []
        self._sidebar_incremental = 0

        # Clean up output directory and recreate them
        try:
            shutil.rmtree(self.output_dir)
        except FileNotFoundError:
            pass
        os.makedirs(self.btd_dir)

    def add_template(self, name, content, alter_name=False):
        """ Add a custom template """
        # Try to create the directory
        templates_dir = os.path.join(self.source_dir, "__btd_templates__")
        os.makedirs(templates_dir, exist_ok=True)

        # Altering the name prevents conflicts
        if alter_name:
            name = "__btd_"+name+"__"
        name += ".html"

        # Save the file
        with open(os.path.join(templates_dir, name), "w") as f:
            f.write(content)

    def add_sidebar(self, content):
        """ Add a custom sidebar """
        self._sidebar_incremental += 1
        name = "sidebar_"+str(self._sidebar_incremental)

        self.add_template(name, content, True)
        self._sidebars.append("__btd_"+name+"__.html")

    def execute(self):
        """ Execute the process """
        try:
            self._obtain_source()
            self._call_hooks()
            self._add_extra_config()
            self._execute_build()
        finally:
            self._cleanup()

    def _obtain_source(self):
        """ Obtain the source code """
        # Get the source obtainer provider
        try:
            name = self.config["source"]["provider"]
        except KeyError:
            raise BuildError("Please specify a source provider")

        try:
            provider = self.builder._source_providers[name]
        except KeyError:
            raise BuildError("Invalid source provider: {}".format(name))

        # Redefine source_dir to avoid having the config["directory"] in it
        source_dir = os.path.join(self.btd_dir, "source")
        provider(self.config, source_dir)  # Obtain the source

    def _call_hooks(self):
        """ Call all the hooks """
        for hook in self.builder._hooks:
            hook(self.builder, self)  # Call the hook

    def _add_extra_config(self):
        """ Append to the documentation's config file the new config """
        extra_conf = utils.get_resource("extra_conf.py", {
            "sidebars": json.dumps(self._sidebars),
        })

        # Append the extra configuration to the configuration file
        with open(os.path.join(self.source_dir, "conf.py"), "a") as f:
            f.write(extra_conf)

    def _execute_build(self):
        """ Execute the build """
        src_dir = self.source_dir
        out_dir = self.output_dir
        dt_dir = os.path.join(self.btd_dir, 'doctrees')

        # Build the documentation with Sphinx
        builder = sphinx.application.Sphinx(src_dir, src_dir, out_dir, dt_dir,
                                            "dirhtml", status=None,
                                            warning=None)
        builder.build(True)

    def _cleanup(self):
        """ Execute some cleanup """
        try:
            shutil.rmtree(self.btd_dir)
        except FileNotFoundError:
            pass
