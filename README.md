# Description
This tool analyze text files in a directory (which was specified
by user) and it's sub folders. Statistics by words count is gathering for 
each text file was found. Then a histogram will be building by this
 statistics.

# Installing
#### Using built *.whl:
```
1. Download the latest version of `*.whl` from:
https://github.com/pkomissarov91/histogramer/releases
2. Install it:
pip install --upgrade path_to_wheel.whl 
```

#### Using sources:
```
1. rm -r build dist histogramer.egg-info (macOs, Linux) 
or RMDIR /Q/S build dist histogramer.egg-info (Windows)
2. python setup.py bdist_wheel
3. pip install --upgrade dist/*.whl
```

# Usage
`python -m histogramer --help`  

# Compatibility
This tool tested using python 3.6.8 virtual environment in Windows 10 and macOS
 Catalina operation systems both.

# Issues
Please, report about any issues to:
`https://github.com/pkomissarov91/histogramer/issues/new/choose` with
 `~/.histogramer` file attached.

# Example
![](Images/histogram_example.png)
