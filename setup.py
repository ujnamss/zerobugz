import setuptools

setuptools.setup(
    name = "zerobugz",
    version = "0.0.2",
    author = "Manjunath Somashekar",
    author_email = "ujnamss@gmail.com",
    packages = ["zerobugz"],
    description = "A simple parameterized annotation helper for the 0bugz synthetic data generation API",
    url = "http://pypi.python.org/pypi/zerobugz/",
    keywords = ["synthetic", "data", "generation"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
Obugz python integration via parameterized annotation
-----------------------------------------------------

This version requires Python 3 or later; a Python 2 version is available separately.
""",
    install_requires=[
        "requests",
    ],
)
