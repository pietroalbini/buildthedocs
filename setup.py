#!/usr/bin/python3
"""
~~~~~~~~~~~~
BuildTheDocs
~~~~~~~~~~~~

*A Sphinx documentation building tool on steroids.*

BuildTheDocs is a tool which helps building Sphinx_ documentation for multiple
versions of a project. It builds the documentation of multiple versions with
only one command, while customizing the documentation, for example adding a
simple version chooser.

It’s also licensed under the MIT license, allowing you to customize it as you
wish.

If you want to learn more about it, you should start reading the
documentation_.

.. _Sphinx: http://sphinx-doc.org
.. _documentation: http://buildthedocs.pietroalbini.io
"""


import setuptools

setuptools.setup(
    name = "buildthedocs",
    version = "1.0",
    url = "http://buildthedocs.pietroalbini.io",

    license = 'MIT',

    author = "Pietro Albini",
    author_email = "pietro@pietroalbini.io",

    description = "A Sphinx documentation building tool on steroids.",
    long_description = __doc__,

    install_requires = [
        'sphinx',
        'jinja2',
        'pyyaml',
        'pygit2',
        'click',
    ],

    packages = [
        'buildthedocs',
    ],

    entry_points = {
        'console_scripts': [
            'buildthedocs = buildthedocs.__main__:main',
        ],
    },

    include_package_data = True,
    zip_safe = False,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Sphinx',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Documentation',
    ],
)
