import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensify",
    author="Dev Shah",
    author_email="devshah1032@gmail.com",
    description="A python package which converts your tenses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeRustyPro/Tensify",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)