"""
For package installation only
"""
import setuptools


def get_readme():
    """
    get long dist description from README.md
    :return: content of README.md file
    """
    with open("README.md") as file:
        return file.read()


def get_requirements(requirements_file):
    """
    get requirements for dist installation
    :return: content of requirements_main.txt file
    """
    with open(requirements_file) as file:
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
        install_requires=get_requirements("requirements_main.txt"),
        long_description=get_readme(),
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        python_requires=">=3.6.8",
        tests_require=get_requirements("requirements_tests.txt"),
        url="https://github.com/pkomissarov91/histogramer/")
