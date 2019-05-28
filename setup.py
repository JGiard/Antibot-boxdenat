import re

from setuptools import setup, find_packages

with open('src/boxdenat/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    assert version is not None

setup(name='Boxdenat',
      version=version,
      author='Jean Giard',
      license='LGPL',
      classifier=[
          'Programming Language :: Python :: 3'
      ],
      entry_points={
          'antibot': ['botdenat=botdenat.plugin:Box']
      },
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=[
          'antibot',
          'pymongo',
          'pynject',
          'autovalue',
          'pyckson',
          'arrow',
          'requests',
          'beautifulsoup4'
      ],
      )
