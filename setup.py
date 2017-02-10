#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.7',
    'pubmedasync>=0.1.0',
]

test_requirements = [
]

setup(
    name='pubmed_authors',
    version='0.1.0',
    description="Search for authors publishing on a topic",
    long_description=readme + '\n\n' + history,
    author="Pokey Rule",
    author_email='pokey.rule@gmail.com',
    url='https://github.com/pokey/pubmed_authors',
    packages=[
        'pubmed_authors',
    ],
    package_dir={'pubmed_authors':
                 'pubmed_authors'},
    entry_points={
        'console_scripts': [
            'pubmed_authors=pubmed_authors.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pubmed_authors',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
