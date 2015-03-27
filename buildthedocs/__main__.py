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
def main(config, version, output):
    """ Build the documentations """
    # Default output path is ./build
    if output == "":
        output = os.path.realpath("build")

    buildthedocs.build(config, *version, output=output)
