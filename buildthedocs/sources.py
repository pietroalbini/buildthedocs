"""
    buildthedocs.sources
    Definition of default source providers

    Copyright (c) 2015 Pietro Albini
    Licensed under MIT license
"""

import os
import urllib.request
import shutil

import pygit2


def obtain_git(config, dest):
    """ Obtain the source code from a git repository """
    pygit2.clone_repository(config["source"]["url"], dest, checkout_branch=
                            config["source"]["checkout"])


def obtain_url(config, dest):
    """ Obtain the source code from an HTTP url """
    # Download the archive
    archive_dest = os.path.join(dest, '__temp_download__')
    urllib.request.urlretrieve(config["source"]["url"], archive_dest)

    # Extract the archive and remove it
    shutil.unpack_archive(archive_dest, dest, config["source"]["compression"])
    os.unlink(archive_dest)


def obtain_local(config, dest):
    """ Obtain the source from the local filesystem """
    shutil.copytree(config["source"]["path"], dest)


_available = {
    "git": obtain_git,
    "url": obtain_url,
    "local": obtain_local,
}
