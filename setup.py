from setuptools import setup

import pygametemplate


setup(
    name="pygametemplate",
    version=pygametemplate.__version__,
    description=pygametemplate.__doc__,
    url="https://github.com/AndyDeany/pygame-template",
    author=pygametemplate.__author__,
    author_email="oneandydean@hotmail.com",
    packages=("pygametemplate",)
    install_requires=(
        "pygame>=1.9.3"
    ),
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: pygame"
    )
)
