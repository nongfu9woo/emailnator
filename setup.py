# setup.py
from setuptools import setup, find_packages

setup(
    name="emailnator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    author="repollo",
    author_email="repollo.marrero@gmail.com",
    description="A Python wrapper for the Emailnator temporary email service.",
    keywords="emailnator wrapper temporary email",
    url="https://github.com/repollo/emailnator",
)
