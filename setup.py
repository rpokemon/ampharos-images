import re

from setuptools import setup

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("ampharos/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

readme = ""
try:
    with open("README.rst") as f:
        readme = f.read()
except FileNotFoundError:
    readme = "No Readme"

setup(
    name="ampharos_images",
    author="bijij",
    url="https://github.com/rpokemon/ampharos_images",
    project_urls={
        "Documentation": "",
        "Issue tracker": "https://github.com/rpokemon/ampharos_images",
    },
    version=version,
    packages=["ampharos_images"],
    license="MIT",
    description="Images for the ampharos database",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    dependency_links=["http://github.com/rpokemon/ampharos/master#egg=ampharos"],
    install_requires=requirements,
    python_requires=">=3.10.0",
)
