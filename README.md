# EZPATHS: Shorthand path modification
![Tests](https://github.com/Gastropod/ezpaths/actions/workflows/ci.yml/badge.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ezpaths.svg)](https://pypi.python.org/pypi/ezpaths/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Gastropod/ezpaths/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/Gastropod/ezpaths.svg)](https://GitHub.com/Gastropod/ezpaths/graphs/contributors/)

### ezpaths
Python module which provides shorthand methods for frequent os.path one-liners

Developed because nested os.path functions can be long and difficult to read.


# Setup


## Requirements

* Python 3+

## Installation


Install it directly into an activated virtual environment with pip:

```text
$ pip install ezpaths
```


# Usage


```python
import ezpaths # Importing to use module installation as example path
from ezpaths import Path # Typical import
```

#### Create a path object by initializing with a path string


```python
# Create path objecet from this file path
path_insatall = Path(ezpaths.__file__)
print('path_insatall: ', path_insatall)
```

    path_insatall:  C:\Users\Brad\Anaconda3\envs\stonks\lib\site-packages\ezpaths\__init__.py
    

#### Use the <code>.dir()</code> method to return the path (type: path) to the parent directory 


```python
# Get parent directory path
install_dir = path_insatall.dir()
print('install_dir: ', install_dir)
```

    install_dir:  C:\Users\Brad\Anaconda3\envs\stonks\lib\site-packages\ezpaths
    

#### The <code>.dir()</code> method can be used to ascend multiple levels
* Use an integer in the dir method arguments to call recursively
* Since a path object is returned, calls to dir can also be chained


```python
# Go up multiple directories
libraries_folder_1 = path_insatall.dir(2)
libraries_folder_2 = path_insatall.dir().dir().dir()
print('libraries_folder_1: ', libraries_folder_1)
print('libraries_folder_2: ', libraries_folder_2)
```

    libraries_folder_1:  C:\Users\Brad\Anaconda3\envs\stonks\lib
    libraries_folder_2:  C:\Users\Brad\Anaconda3\envs\stonks\lib
    

#### To get just the name of the current directory (type: string), use the <code>.dirname()</code> method


```python
# Get parent directory name
dirname = path_insatall.dirname()
print('dirname: ', dirname)
```

    dirname:  ezpaths
    

#### Get full filename or just name or extension


```python
# filenames
filename = path_insatall.filename()
print('filename: ', filename)
name = path_insatall.name()
print('name: ', name)
ext = path_insatall.ext()
print('ext: ', ext)
```

    filename:  __init__.py
    name:  __init__
    ext:  .py
    

#### The == operator will check if the absolute address of a path or path-string are the same


```python
# Check if same path
same = libraries_folder_1 == libraries_folder_2
print('same (matching): ', same)
same = libraries_folder_1 == path_insatall
print('same (non-matching): ', same)
```

    same (matching):  True
    same (non-matching):  False
    

#### The + and / operators will join paths


```python
path_ezpaths = install_dir / filename
print('path_ezpaths: ', path_ezpaths)
path_ezpaths = path_ezpaths.dir() + path_ezpaths.filename()
print('path_ezpaths: ', path_ezpaths)
```

    path_ezpaths:  C:\Users\Brad\Anaconda3\envs\stonks\lib\site-packages\ezpaths\__init__.py
    path_ezpaths:  C:\Users\Brad\Anaconda3\envs\stonks\lib\site-packages\ezpaths\__init__.py
    

#### A path object is true if the target exists


```python
# Check if path exists
exists_file = bool(path_insatall)
print('exists_file: ', exists_file)
exists_dir = bool(install_dir)
print('exists_dir: ', exists_dir)
exists_random = bool(install_dir / "random.txt")
print('exists_random: ', exists_random)
```

    exists_file:  True
    exists_dir:  True
    exists_random:  False
    

