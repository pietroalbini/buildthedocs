"""
    buildthedocs
    Entry point of BuildTheDocs

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import os
import functools

import yaml

from buildthedocs import initializer
from buildthedocs.builder import Builder


# Setup the global collector
_collector = initializer.Collector()
_collector.collect('buildthedocs')

# Setup the global initializer (registering stuff at runtime)
_initializer = initializer.Initializer()
_collector.append("buildthedocs:runtime", _initializer)


def build(config, *versions, output="build", dists=None):
    """ Build from a configuration file """
    # If the passed configuration is a path to a file load the content of it
    # as YAML
    if isinstance(config, str) and os.path.exists(config):
        with open(config) as f:
            config = yaml.load(f.read())

    builder = Builder(config, output, dists)

    return builder.build(*versions)


def source_provider(name, func=None):
    """ Register a new source provider """
    def decorator(func):
        _initializer.register_source_provider(name, func)
        return func

    # Because of this, this function will act both as a decorator and as a
    # normal API (func is None if it's called as a decorator)
    if func is None:
        return decorator
    else:
        return decorator(func)


def hook(func):
    """ Register a new hook """
    # This is both a decorator and a normal API
    _initializer.register_hook(func)
    return func


__all__ = [
    'Builder',
    'build',
    'source_provider',
    'hook',
]
