# DictClass [![Build Status](https://travis-ci.org/dhilst/py-dictclass.svg?branch=master)](https://travis-ci.org/dhilst/py-dictclass) [![PyPI](https://img.shields.io/pypi/v/dictclass.svg)](https://pypi.python.org/pypi/dictclass/0.0.1) [![GitHub license](https://img.shields.io/github/license/dhilst/py-dictclass.svg)](https://github.com/dhilst/py-dictclass/blob/master/LICENSE)

Create dictionaries with the class syntax with support for inheritance.

# Motivation

1. I hate to type curlybraces, quotes and colons.
2. It's common to use dicts as configuration, these dicts may be very similar differing only
   by some few keys. So having inheritance here is good.
3. The class syntax is much more readable.

# Usage

Extend `DictClass`. The keys are the class attributes and the values, duh, are the values.

Example:
```python

from dictclass import DictClass

class MyDict(DictClass):
    key1 = 'value1'
    key2 = 'value2'

class MyOtherDict(MyDict):
    key1 = 'notvalue1'  # Key can be overwritten
    key3 = 'value3'


MyOtherDict.as_dict()  # return a dynamically created dict
```
