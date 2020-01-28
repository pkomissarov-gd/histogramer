# Compatibility #
This tool has tested using python 3.6.8 virtual environment in Windows 10 and 
macOS Catalina operation systems both.

# Description #
This tool analyze text files in a directory (which was specified
by user) and it's sub folders. Statistics by words count is gathering for 
each text file was found. Then a histogram will be building by this
 statistics.
 
 # Example #
![](Images/histogram_example.png)

# Installation #
* #### Using a `*.whl` dist: ####
    * Download the latest `*.whl` version from a
    [releases page](https://github.com/pkomissarov91/histogramer/releases).
    * Install it: `pip install --upgrade path_to_wheel.whl`.

* #### Using sources: ####
    * Remove a `*.whl` dist: `rm -r build dist histogramer.egg-info` 
    (macOs, Linux) or `RMDIR /Q/S build dist histogramer.egg-info` (Windows). 
    * Rebuild a `*.whl` dist: `python setup.py bdist_wheel`.
    * Install a new `*.whl` dist: `pip install --upgrade dist /*.whl`.

# Issues #
Please, report about any issues to an 
[issues page](https://github.com/pkomissarov91/histogramer/issues/new/choose)
with a `~/.histogramer` file attached.

# Usage #
Run a `python -m histogramer --help` script.
