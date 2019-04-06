"""Setup configuration."""
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    README = fh.read()
setup(
    name="sampleclient",
    version="0.0.0",
    author="Joakim Sorensen",
    author_email="hi@ludeeus.com",
    description="Sample Client lib.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/sampleclient",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
