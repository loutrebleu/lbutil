# coding: utf-8

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='lbutil',
    version='0.0.1',
    description="Utility functions",
    long_description=readme,
    author='yoshikawa',
    author_email='yoshikawa@loutrebleu.com',
    url='https://github.com/loutrebleu/lbutil',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=reqs
)
