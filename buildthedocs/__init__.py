"""
    buildthedocs
    Entry point of BuildTheDocs

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import yaml
import os

from buildthedocs.builder import Builder


def build(config, *versions, output="build", source_providers=None):
    """ Build from a configuration file """
    # If the passed configuration is a path to a file load the content of it
    # as YAML
    if isinstance(config, str) and os.path.exists(config):
        with open(config) as f:
            config = yaml.load(f.read())

    builder = Builder(config, output)

    # Register source providers if provided
    if source_providers is not None:
        for name, provider in source_providers.items():
            builder.register_source_provider(name, provider)

    return builder.build(*versions)


__all__ = [
    'Builder',
    'build',
]
