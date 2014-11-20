#!/usr/bin/env python

from setuptools import setup

setup(name='plumbing-atkinson-server',
      version='0.2',
      description='A Flask based HTTP pony for dithering images using an Atkinson filter',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-atkinson-server',
      requires=[
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.34',
          'https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson/tarball/master#egg=cooperhewitt.roboteyes.atkinson-0.2',
      ],
      install_requires=[
          'cooperhewitt.flask',
          'cooperhewitt.roboteyes.atkinson',
      ],
      packages=[],
      scripts=[
          'scripts/atkinson-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-atkinson-server/tarball/master#egg=plumbing-atkinson-server-0.2',
      license='BSD')
