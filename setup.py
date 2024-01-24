# coding: utf-8

"""
    Spryngtime Usage Analytics & Billing API

    Spryngtime Usage Analytics & Billing API

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "spryngtime-azure-openai-python"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "aiohttp >= 3.9.1",
    "aiosignal >= 1.3.1",
    "annotated-types >= 0.6.0",
    "anyio >= 4.2.0",
    "async-timeout >= 4.0.3",
    "attrs >= 23.2.0",
    "certifi >= 2023.11.17",
    "cffi >= 1.16.0",
    "cryptography >= 41.0.7",
    "distro >= 1.9.0",
    "exceptiongroup >= 1.2.0",
    "frozendict >= 2.4.0",
    "frozenlist >= 1.4.1",
    "h11 >= 0.14.0",
    "httpcore >= 1.0.2",
    "httpx >= 0.26.0",
    "idna >= 3.6",
    "multidict >= 6.0.4",
    "openai == 0.28.1",
    "pycparser >= 2.21",
    "pydantic >= 2.5.3",
    "pydantic_core >= 2.14.6",
    "python-dateutil >= 2.8.2",
    "python-dotenv >= 1.0.1",
    "six >= 1.16.0",
    "sniffio >= 1.3.0",
    "spryngtime-analytics-sdk >= 1.1.5",
    "spryngtime-analytics-sdk-python-sdk >= 1.0.1",
    "tqdm >= 4.66.1",
    "typing_extensions >= 4.9.0",
    "urllib3 >= 1.26.18",
    "yarl >= 1.9.4"
]

setup(
    name=NAME,
    version=VERSION,
    description="Spryngtime Usage Analytics & Billing API",
    author="Spryngtime",
    author_email="michael@usespryngtime.com",
    url="https://github.com/azianmike/spryngtime-analytics-sdk/tree/main/python",
    keywords=["Konfig", "Spryngtime Usage Analytics & Billing API OpenAI wrapper"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown'
)