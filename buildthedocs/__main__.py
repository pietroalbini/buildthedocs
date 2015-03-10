import os
import click
import buildthedocs.builder


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

    project = buildthedocs.builder.Project(config, output)

    # If no version was provided, build the entire project
    # Else build each specified version
    if len(version) == 0:
        project.build()
    else:
        for one in version:
            try:
                project.build(one)
            except ValueError:
                error("version {} not found", one)
