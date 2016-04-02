"""
    buildthedocs.hooks
    Default hooks of BuildTheDocs

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

from buildthedocs import utils


def add_versions_chooser(builder, process):
    """ Add the version chooser to the documentation """
    sidebar = utils.get_resource("sidebar_versions.html", {
        "versions": builder.ordered_versions,
        "current_version": process.version,
    })

    process.add_sidebar(sidebar)


def add_warning(builder, process):
    """ Add a warning to the documentation, if needed """
    # Don't add anything if no warning was provided
    if process.config["warning"] is None:
        return

    new_layout = utils.get_resource("layout.html", {
        "warning": process.config["warning"],
    })

    process.add_template("layout", new_layout)
