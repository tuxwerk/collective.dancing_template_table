# -*- coding: utf-8 -*-
"""Installer for the collective.dancing_template_table package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.dancing_template_table',
    version='1.0',
    description="TABLE-based template for collective.dancing",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.0",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='plone dancing newsletter template',
    author='Marek Kralewski',
    author_email='info@tuxwerk.de',
    url='https://github.com/tuxwerk/collective.dancing_template_table',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'z3c.jbot',
        'collective.dancing',
    ],
    extras_require={
        'test': [
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
