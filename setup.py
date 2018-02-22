from setuptools import (
    setup,
    find_packages,
)

setup(
    name="thoughtfulsoup",
    version = "0.0.1",
    author="Derek Chan",
    author_email='dchan3@hawaii.edu',
    description="beautifulsoup4 fork",
    long_description="""TLDR: This is pretty much a fork of BeautifulSoup4, but thoughtfully extended.""",
    license="MIT",
    packages=find_packages(exclude=['tests*']),
    extras_require = {
        'lxml' : [ 'lxml'],
        'html5lib' : ['html5lib'],
    },
    use_2to3 = True,
    classifiers=["Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 'Programming Language :: Python :: 3',
                 "Topic :: Text Processing :: Markup :: HTML",
                 "Topic :: Text Processing :: Markup :: XML",
                 "Topic :: Text Processing :: Markup :: SGML",
                 "Topic :: Software Development :: Libraries :: Python Modules",
             ],
)
