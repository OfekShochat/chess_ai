import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yannl",
    version = "0.0.1",
    author = "Ofek Shochat",
    author_email = "o@shoch.at",
    description = ("a python ai with a lot of plugins like a chess engine, rnn, cnn and I will post more!"),
    license = "BSD",
    keywords = ["ai", "neural", "networks", "nn", "plugins", "nn plugins"],
    url = "http://packages.python.org/",
    py_modules=['numpy', 'requests'],
    long_description=read('README.md'),
    package_dir = {"":"src"},
    License="GPL-3.0 License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPL-3.0 License",
    ],
)