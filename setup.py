from setuptools import setup

import pygametemplate


setup(
    name="pygametemplate",
    version=pygametemplate.__version__,
    license="MIT",
    description=pygametemplate.__doc__,
    url="https://github.com/AndyDeany/pygame-template",
    download_url=pygametemplate.__download_url__,
    author=pygametemplate.__author__,
    author_email=__author_email__,
    packages=(pygametemplate.__name__,),
    keywords=("pygame", "template", "gamedev"),
    install_requires=(
        "pygame>=1.9.3",
    ),
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: pygame",
    )
)
