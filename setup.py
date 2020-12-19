import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SpaPy-Jim Graham", # Replace with your own username
    version="1.0.0",
    author="Jim Graham, Nicholas Klein-Baer, Melody Dick",
    author_email="james.graham@humboldt.edu, msd9@humboldt.edu",
    description="Fast and fun geospatial library based on open source software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jg2345/SpaPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: FSF Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)