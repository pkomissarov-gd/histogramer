# Description
This tool analyze text files in the directory (which specified
by user) and it's sub folders. Statistics by words count gather for 
each text file was found. Then a histogram is creating by this statistics.

# Installing
#### From prebuilt wheel
1. Download `*.whl` from the latest [release]:
https://github.com/pkomissarov91/histogramer/releases
2. Install with:
```
pip install --upgrade path_to_wheel.whl 
```

#### From sources
```
rm -r build dist (macOs, Linux) or RMDIR /Q/S build dist (Windows)
python setup.py bdist_wheel
pip install --upgrade dist/*.whl
```

# Usage
`python -m histogramer --help`  

# Compatibility
This tool was tested in python 3.6.8 virtual environment in Windows 10 and
 macOS Catalina both.

# Issues
Please report any issues. Make sure to include `~/.histogramer` file, 
which contains a full log of *latest* runs.
