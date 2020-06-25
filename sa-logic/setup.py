"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='K8S Service logic',
    version='0.0.1',
    description='Source code for the K8S Service logic.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Sebastien MASCHA',
    author_email='s.mascha@samsung.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Flask API K8S',
    packages=find_packages(),
    install_requires=['Flask',
                      'Flask_assets'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install=wsgi:__main__',
        ],
    }
)
