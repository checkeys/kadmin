# coding=utf-8

from urllib.parse import urljoin

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

from ringwork.attribute import __author__
from ringwork.attribute import __author_email__
from ringwork.attribute import __description__
from ringwork.attribute import __project__
from ringwork.attribute import __urlhome__
from ringwork.attribute import __version__

__urlcode__ = __urlhome__
__urldocs__ = __urlhome__
__urlbugs__ = urljoin(__urlhome__, "issues")


def all_requirements():
    def read_requirements(path: str):
        with open(path, "r", encoding="utf-8") as rhdl:
            return rhdl.read().splitlines()

    requirements = read_requirements("requirements.txt")
    return requirements


class CustomInstallCommand(install):
    """Customized setuptools install command"""

    def run(self):
        install.run(self)  # Run the standard installation
        # Execute your custom code after installation


setup(
    name=__project__,
    version=__version__,
    description=__description__,
    url=__urlhome__,
    author=__author__,
    author_email=__author_email__,
    project_urls={"Source Code": __urlcode__,
                  "Bug Tracker": __urlbugs__,
                  "Documentation": __urldocs__},
    packages=find_packages(include=["ringwork*"], exclude=["ringwork.unittest"]),  # noqa:E501
    package_data={"ringwork.static": ["*.svg"],
                  "ringwork.static.icons": ["*.svg"],
                  "ringwork.static.styles": ["*.css"],
                  "ringwork.static.javascript": ["*.js"],
                  "ringwork.templates": ["*.html"],
                  "ringwork.translate": ["*.xlc"]},
    install_requires=all_requirements(),
    cmdclass={
        "install": CustomInstallCommand,
    }
)
