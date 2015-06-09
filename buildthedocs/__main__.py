"""
    buildthedocs.__main__
    Console entry point for buildthedocs

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import os
import click
import buildthedocs


def error(message, *replace):
    """ Show an error message and exit """
    click.echo("buildthedocs: error: {}".format(*replace), err=True)
    exit(1)


@click.command()
@click.argument("config")
@click.argument("version", nargs=-1)
@click.option("-o", "--output", help="The output directory", default="")
@click.option("--dist", "extra_dists", multiple=True, default=None,
              help="Allow an extra distribution")
@click.option("--default-dists", help="", is_flag=True)
def main(config, version, output, default_dists, extra_dists):
    """ Build the documentations """
    # Default output path is ./build
    if output == "":
        output = os.path.realpath("build")

    dists = [] if default_dists or extra_dists else None
    if default_dists:
        dists += ["buildthedocs:sources", "buildthedocs:hooks"]
    if dists is not None:
        dists += extra_dists

    buildthedocs.build(config, *version, output=output, dists=dists)
