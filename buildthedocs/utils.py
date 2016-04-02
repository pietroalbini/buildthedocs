"""
    buildthedocs.utils
    Some random utilities

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import pkg_resources
import jinja2


def get_resource(path, jinja_context=None):
    """ Get a resource from the package, eventually building it with jinja """
    path = "resources/"+path
    raw = pkg_resources.resource_string("buildthedocs", path).decode("utf-8")

    # If jinja_context is provided, parse the template
    if jinja_context is not None:
        template = jinja2.Template(raw)
        return template.render(jinja_context)

    return raw
