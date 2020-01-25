"""
For package installation only
"""
import setuptools

with open("README.md") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
        name="histogramer",
        version="1.0.0",
        author="Petr Komissarov",
        author_email="pkomissarov@griddynamics.com",
        description="Tool for histogram building by words count in files",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/pkomissarov91/histogramer/",
        packages=setuptools.find_packages(),
        install_requires=open("requirements.txt").read(),
        classifiers=[
            "Programming Language :: Python :: 3.6.8",
            "Operating System :: OS Independent"],
        python_requires=">=3.6.8")
