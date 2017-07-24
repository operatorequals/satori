#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='satori',
    version='0.01',
    description='A filesystem image suite',
    long_description=long_description,
    url='https://github.com/operatorequals/satori',
    download_url='https://github.com/operatorequals/satori/archive/master.zip',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
      'Operating System :: POSIX :: Linux'
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='John Torakis',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='john.torakis@gmail.com',
    entry_points = {
        'console_scripts' : [ "satori-browser=satori.satori-browser:main",
                        "satori-differ=satori.satori-differ:main",
                        "satori-imager=satori.satori-imager:main",
                        "satori-remote=satori.satori-remote:main",
                        ]
                    }
)