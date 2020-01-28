"""
For package installation only
"""
import setuptools

with open("README.md") as desc_file:
    DESCRIPTION = desc_file.read()

with open("requirements.txt") as req_file:
    REQUIREMENTS = req_file.read()

setuptools.setup(
        name="histogramer",
        version="1.0.4",
        author="Petr Komissarov",
        author_email="pkomissarov@griddynamics.com",
        description="Tool for histogram building by words count in files",
        long_description=DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/pkomissarov91/histogramer/",
        packages=setuptools.find_packages(),
        install_requires=REQUIREMENTS,
        classifiers=[
            "Programming Language :: Python :: 3.6.8",
            "Operating System :: OS Independent"],
        python_requires=">=3.6.8")
