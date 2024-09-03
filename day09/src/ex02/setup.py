from setuptools import setup, Extension
from Cython.Build import cythonize

matrix_module = [
    Extension("matrix", ["multiply.pyx"]),
]

setup(
    name="matrix",
    version="1.0",
    ext_modules=cythonize(matrix_module),
)
