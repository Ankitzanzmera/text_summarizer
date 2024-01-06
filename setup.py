from setuptools import find_packages,setup

__version__ = "0.0.0"
AUTHOR_NAME = "Ankitzanzmera"
AUTHOR_EMAIL = "22msrds052@jainuniversity.ac.in"
SRC_REPO = "text_summarizer"

setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="End to End NLP Project",
    package_dir= {"":"src"},
    packages = find_packages(where = "src")
)  