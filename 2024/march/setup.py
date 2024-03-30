# setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("hooks2.pyx"))#, compiler_directives={"language_level": "3"}))