from setuptools import Extension, setup

calculator_module = Extension('calculator', ["calculator.c"])
setup(
    name='calculator',
    version='1.0',
    ext_modules=[calculator_module]
)
