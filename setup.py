import os
from setuptools import setup, find_packages
from importlib.machinery import SourceFileLoader


module = SourceFileLoader(
    "version", os.path.join("aio_pika", "version.py")
).load_module()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="rabbitmq-client",
    version=module.__version__,
    author=module.__author__,
    author_email=module.team_email,
    license=module.package_license,
    description=module.package_info,
    long_description_content_type="text/markdown",
    long_description=long_description,
    keywords=["pika", "rabbitmq", "amqpy"],
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: BSD-3-Clause",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(exclude=["tests"]),
    package_data={"rabbitmq_client": ["requirements.txt"]},
    install_requires=[
        "pika~=1.3.1"
    ],
    python_requires=">3.6, <4",
    extras_require={
        "develop": [
            "aiomisc~=16.0",
            "coverage!=4.3",
            "coveralls",
            "pylava",
            "pytest",
            "pytest-cov",
            "shortuuid",
            "nox",
            "sphinx",
            "sphinx-autobuild",
            "timeout-decorator",
            "tox>=2.4",
        ],
    },
    project_urls={
        "Source": "https://github.com/mad-underground/rabbitmq-client",
    },
)