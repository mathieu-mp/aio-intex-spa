"""Setup configuration."""
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    README = fh.read()
setup(
    name="intex-spa",
    version="0.0.0",
    author="Mathieu Payrol",
    author_email="intex-spa@payrol.fr",
    description="Intex Spa wifi client",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mathieu-mp/intex-spa",
    packages=find_packages(),
    install_requires=["asyncio"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
