# Copyright (c) 2022. Leehands Studio
#
from __future__ import print_function
import os

from setuptools import setup ,find_packages

if __name__ == '__main__':
    setup(
        name='lh-tinylib',
        version="0.0.1",
        description="Leehands Tiny Library for example",
        author="Lee Namhun",
        author_email="leehands83@icloud.com",
        url="https://github.com/leehands-society/lh-tinylib.git",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: Linux',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
        ],
        install_requires=[],
        packages=find_packages(),
    )
