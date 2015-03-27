"""
    buildthedocs.builder
    Logic of the documentation builder

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import subprocess
import shutil
import os

import yaml
import sphinx.application
import pygit2
import pkg_resources
import jinja2

import buildthedocs.sources


class Builder:
    """ Instance of a builder """

    def __init__(self, config, output_to):
        self.versions = {version["name"]: version
                         for version in config["versions"]}
        self.ordered_versions = config["versions"]

        self._output_to = output_to
        self._source_providers = {}

        # Register default source providers
        for name, provider in buildthedocs.sources._available.items():
            self.register_source_provider(name, provider)

    def register_source_provider(self, name, provider):
        """ Register a new source provider """
        # Do some validation
        if name in self._source_providers:
            raise NameError('A source provider with the name "{}" already '
                            'exists'.format(name))
        if not callable(provider):
            raise ValueError('The provider must be callable')

        self._source_providers[name] = provider

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

        return process.output


class BuildProcess:
    """ A build process """

    def __init__(self, builder, version, details):
        self._details = details
        self.builder = builder
        self.version = version

        self.executed = False
        self.output = os.path.join(builder._output_to, version)

        # Clean up output directory and recreate dirs
        try:
            shutil.rmtree(self.output)
        except FileNotFoundError:
            pass
        os.makedirs(os.path.join(self.output, "__buildthedocs__"))

    def execute(self):
        """ Execute the process """
        try:
            self._obtain_source()
            self._patch_documentation()
            self._execute_build()
        finally:
            self._cleanup()

    def _obtain_source(self):
        """ Obtain the source code """
        # Get the source obtainer provider
        try:
            provider = self.builder._source_providers[
                                        self._details["source"]["provider"]]
        except KeyError:
            raise RuntimeError("Invalid source provider: {}".format(
                               self._details["source"]["provider"]))

        # Obtain the source
        dest = os.path.join(self.output, "__buildthedocs__", "source")
        provider(self._details, dest)

    def _patch_documentation(self):
        """ Patch the documentation to obtain the result we want """
        base = os.path.join(self.output, "__buildthedocs__", "source",
                            self._details["directory"])

        self._add_template(base, "sidebar_versions", {
            "versions": self.builder.ordered_versions,
            "current_version": self.version,
        }, True)

        self._add_template(base, "layout", {
            "warning": self._details["warning"],
        })

        self._add_extra_config(base)

    def _add_template(self, base, name, data, alter=False):
        """ Add a custom template """
        result = self._get_resource(name+".html", data)

        # Try to create the directory
        try:
            os.makedirs(os.path.join(base, "__buildthedocs_templates__"))
        except FileExistsError:
            pass

        # Save the file
        if alter:
            final_name = "__buildthedocs_"+name+"__.html"
        else:
            final_name = name+".html"
        tpl_base = os.path.join(base, "__buildthedocs_templates__")
        self._save_file(tpl_base, final_name, result)

    def _add_extra_config(self, base):
        """ Append to the documentation's config file the new config """
        extra_conf = self._get_resource("extra_conf.py")
        self._save_file(base, "conf.py", extra_conf, "a")

    def _execute_build(self):
        """ Execute the build """
        src_dir = os.path.join(self.output, '__buildthedocs__', 'source',
                               self._details["directory"])
        out_dir = self.output
        dt_dir = os.path.join(self.output, '__buildthedocs__', 'doctrees')

        # Build the documentation with Sphinx
        builder = sphinx.application.Sphinx(src_dir, src_dir, out_dir, dt_dir,
                                            "dirhtml", status=None,
                                            warning=None)
        builder.build(True)

    def _cleanup(self):
        """ Execute some cleanup """
        try:
            shutil.rmtree(os.path.join(self.output, "__buildthedocs__"))
        except FileNotFoundError:
            pass

    def _get_resource(self, path, jinja_vars=None):
        """ Obtain a resource from the package, parse it and return it """
        content = pkg_resources.resource_string("buildthedocs",
                                "resources/"+path).decode("utf-8")

        # Parse it as jinja template if needed
        if jinja_vars is not None:
            template = jinja2.Template(content)
            content = template.render(jinja_vars)

        return content

    def _save_file(self, base, name, content, mode="w"):
        """ Shortcut to save a file """
        with open(os.path.join(base, name), mode) as f:
            f.write(content)
