import setuptools

setuptools.setup(
    name = "buildthedocs",
    version = "1.0a1",

    license = 'MIT',

    author = "Pietro Albini",
    author_email = "pietro@pietroalbini.io",

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
)
