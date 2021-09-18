# -*- coding: utf-8 -*-
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    print("error to load the setup function from package setup tools")
    from distutils.core import setup

setup(
    name='ks_barrage',
    version='0.0.14',
    description='a ks barrage',
    author='jayden',
    author_email='282669595@qq.com',
    url='https://qq.com/',

    classifiers=[
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
    ],
    packages=find_packages(),
    install_requires=[
        'redis',
    ],
)
