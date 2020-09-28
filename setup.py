import io
import os
import sys
from setuptools import Command, find_packages, setup
from shutil import rmtree

HERE = os.path.abspath(os.path.dirname(__file__))

NAME = "esp-trainer"
DESCRIPTION = "ESP trainer that runs in your terminal"
AUTHOR = "Daniel Spajic"
AUTHOR_EMAIL = "daniel@danieljs.tech"
URL = "https://github.com/dspacejs/cli-esp-trainer"
PYTHON_VERSION = ">=3.8.2"
REQUIRED_DEPS = (
    "colorama >= 0.4.3",
    "tabulate >= 0.8.7",
)


# Get version number
about = {}
PROJECT_SLUG = NAME.lower().replace("-", "_").replace(" ", "_")

with open(os.path.join(HERE, PROJECT_SLUG, "__version__.py")) as f:
    exec(f.read(), about)


# Get long description from README
try:
    with io.open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        os.system(
            "{0} setup.py sdist bdist_wheel --universal".format(sys.executable),
        )

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    python_requires=PYTHON_VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment",
    ],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=REQUIRED_DEPS,
    entry_points={
        "console_scripts": ["esp-trainer=esp_trainer.__main__:main"],
    },
)
