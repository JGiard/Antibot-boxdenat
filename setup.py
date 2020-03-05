import re

from setuptools import setup, find_packages

with open('src/boxdenat/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    assert version is not None

setup(name='antibot-boxdenat',
      version=version,
      author='Jean Giard',
      license='LGPL',
      classifier=[
          'Programming Language :: Python :: 3'
      ],
      entry_points={
          'antibot': ['boxdenat=boxdenat.plugin:BoxPlugin']
      },
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=[
          'antibot',
          'pymongo',
          'pyckson',
          'arrow',
          'requests',
          'beautifulsoup4',
          'injector'
      ],
      )
