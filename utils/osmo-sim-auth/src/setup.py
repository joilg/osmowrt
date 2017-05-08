import os
from setuptools import setup

# A command line tool for (U)SIM authentication
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_pypi_project",
    version = "0.0.4",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    description = ("osmo-sim-auth is a small script that can be used with a smart card"
			"reader to obtain GSM/UMTS authentication parameters from a SIM/USIM"
			"card. "),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://osmocom.org/projects/osmo-sim-auth",
    packages=['card'],
    long_description=read('Card'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
