"""
    buildthedocs.initializer
    Collect initializers and apply them to the Builder

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import pkg_resources

from buildthedocs import sources
from buildthedocs import hooks


class Collector:
    """ Collect initializers """

    def __init__(self):
        self._collected = {}

    def collect(self, entry_point):
        """ Collect from setuptools entry points """
        for one in pkg_resources.iter_entry_points(entry_point):
            loaded = one.load()

            # Create an initializer instance, and fill it
            initializer = Initializer()
            loaded(initializer)
            self._collected[one.dist.key+":"+one.name] = initializer

    def append(self, dist, initializer):
        """ Add an initializer """
        if dist in self._collected:
            raise NameError("An initializer with the {} key already exists"
                            .formate(dist))

        self._collected[dist] = initializer

    def apply(self, obj, only=None):
        """ Apply all collector """
        # If "only" is provided, apply initializers only from that packages
        if only is not None:
            initializers = [value for key, value in self._collected.items()
                            if key in only]
        else:
            initializers = list(self._collected.values())

        for initializer in initializers:
            obj = initializer._apply(obj)
        return obj


class Initializer:
    """ An initializer class

    This will record all the calls made to this class' methods, so them can be
    applied to another object
    """

    def __init__(self):
        self._recorded = []

    def __getattribute__(self, key):
        # Ignore private and magic methods
        if key.startswith('_'):
            return object.__getattribute__(self, key)

        # This stub will be returned, and each call you made to it will be
        # recorded
        def stub(*args, **kwargs):
            # Build a function which calls the wanted method
            def call(obj):
                getattr(obj, key)(*args, **kwargs)
                return obj
            self._recorded.append(call)
        stub.__name__ = key

        return stub

    def _apply(self, obj):
        """ Apply all recorded calls to an object """
        for call in self._recorded:
            obj = call(obj)
        return obj


def sources_initializer(initializer):
    """ Initialize the default source providers of BuildTheDocs """
    # Register default source providers
    initializer.register_source_provider("local", sources.obtain_local)
    initializer.register_source_provider("url", sources.obtain_url)
    initializer.register_source_provider("git", sources.obtain_git)


def hooks_initializer(initializer):
    """ Initialize the default hooks of BuildTheDocs """
    # Register default build hooks
    initializer.register_hook(hooks.add_versions_chooser)
    initializer.register_hook(hooks.add_warning)
