#!/usr/bin/env python

from setuptools import setup


def get_requirements(filename):
    with open(filename) as fp:
        return [
            requirement
            for requirement in fp
            if requirement and not requirement.startswith('#')
        ]


def get_readme_contents():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()


setup(
    name='scrapy-dynamodb',
    version='0.2.3',
    description='AWS DynamoDB pipeline for Scrapy',
    long_description=get_readme_contents(),
    long_description_content_type='text/x-rst',
    author='Alister Cordiner',
    author_email='alister@cordiner.net',
    url='https://github.com/acordiner/scrapy-dynamodb',
    install_requires=get_requirements('requirements.txt'),
    py_modules=['scrapy_dynamodb'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
