from setuptools import setup


version = "0.8.0"
url = "https://github.com/AndyDeany/pygame-template"

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name="pygametemplate",
    version=version,
    license="MIT",
    description="Making making games with Pygame easier :)",
    url=url,
    download_url="{}/archive/v{}.tar.gz".format(url, version),
    author="Andrew Dean",
    author_email="oneandydean@hotmail.com",
    packages=("pygametemplate",),
    keywords=("pygame", "template", "gamedev"),
    install_requires=requirements,
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: pygame",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    )
)
