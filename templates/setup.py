#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from codecs import open
import os

import versioneer


CLASSIFIERS = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
""".strip()

INSTALL_REQUIRES = [
    'click',
    'requests>=2.18',
    'numpy>=1.13',
    'scipy',
    'pillow',
    'ruamel.yaml',
    'future'
]

EXTRAS_REQUIRE = {
    'dev': ['versioneer'],
    'test': ['pytest', 'pytest-cov', 'codecov']
}
EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))

CONSOLE_SCRIPTS = [
    'veros = veros.cli.veros:cli',
    'veros-run = veros.cli.veros_run:cli',
    'veros-copy-setup = veros.cli.veros_copy_setup:cli',
    'veros-resubmit = veros.cli.veros_resubmit:cli',
    'veros-create-mask = veros.cli.veros_create_mask:cli'
]

PACKAGE_DATA = ['assets/*.yml']

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='<packagename>',
    license='MIT',
    author='Employee McEmployeeface (DHI GRAS)',
    author_email='empl@dhigroup.com',
    keywords='python geodata awesome',
    description='Does all the hard things in a simple way',
    long_description=long_description,
    url='https://hardstuff.readthedocs.io',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    package_data={
        '<packagename>': PACKAGE_DATA
    },
    classifiers=[c for c in CLASSIFIERS.split('\n') if c]
)
