"""
For package installation only
"""
import setuptools


def read_file(file_name):
    """
    get content of the file
    :param file_name: name of the file
    :return: content of the file
    """
    with open(file_name) as file:
        return file.read()


setuptools.setup(
        name="histogramer",
        version="1.0.5",
        author="Petr Komissarov",
        author_email="pkomissarov@griddynamics.com",
        classifiers=[
            "Programming Language :: Python :: 3.6.8",
            "Operating System :: OS Independent"],
        description="Tool for histogram building by words count in files",
        install_requires=read_file("requirements_main.txt"),
        long_description=read_file("README.md"),
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        python_requires=">=3.6.8",
        tests_require=read_file("requirements_tests.txt"),
        url="https://github.com/pkomissarov-gd/histogramer")
