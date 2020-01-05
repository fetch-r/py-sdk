import setuptools


def get_long_description():
    with open("README.md", "r") as fh:
        return fh.read()


setuptools.setup(
    name="fetchr",
    version="0.0.1",
    url="https://github.com/fetch-r/py-sdk",
    description="Client for the FetchR ORM",
    license="MIT",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Lavrentios Frobeen",
    author_email="lavrenti@nexys.ch",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests==2.*",
    ],
    entry_points={
        "console_scripts": [
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
