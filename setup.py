import os
import sys
import pbs

try: from distutils.core import setup
except ImportError: from setuptools import setup


if sys.argv[-1] == "test":
    versions = ("2.6", "2.7", "3")
    
    for version in versions:    
        try: py = pbs.Command("python%s" % version)
        except pbs.CommandNotFound: pass
        else:
            print "Testing Python%s" % version
            py("test.py", _fg=True)
            print
    exit(0)


setup(
    name="pbs",
    version=pbs.__version__,
    description="Python subprocess wrapper",
    author="Andrew Moffat",
    author_email="andrew.robert.moffat@gmail.com",
    url="https://github.com/amoffat/pbs",
    license="MIT",
    py_modules=["pbs"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
