#from distutils.core import setup
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='essential_docgen',
    version='0.4',
    packages=['essential_docgen'],
    url='https://github.com/shane-mason/essential-document-generator',
    license='MIT',
    author='scmason',
    author_email='shane.c.mason@gmail.com',
    description='Generate Python objects based on simple but flexible templates',
    long_description=long_description,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
                      # How mature is this project? Common values are
                      #   3 - Alpha
                      #   4 - Beta
                      #   5 - Production/Stable
                      'Development Status :: 3 - Alpha',

                      # Indicate who your project is intended for
                      'Intended Audience :: Developers',
                      'Topic :: Software Development :: Build Tools',

                      # Pick your license as you wish (should match "license" above)
                      'License :: OSI Approved :: MIT License',

                      # Specify the Python versions you support here. In particular, ensure
                      # that you indicate whether you support Python 2, Python 3 or both.
                      'Programming Language :: Python :: 3',
                      'Programming Language :: Python :: 3.3',
                      'Programming Language :: Python :: 3.4',
                      'Programming Language :: Python :: 3.5',
                  ]


)