from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'easytime',
    version = '0.1.0',
    py_modules = ('easytime',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['python-dateutil>=2.1'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/easytime',
    keywords = 'python time simple easy timezone',
    description = 'The simplest python time library ever written.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
