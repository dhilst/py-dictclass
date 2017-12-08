# DictClass

Create dictionaries with the class syntax with support for inheritance.

# Motivation

1. I hate type curlybraces, quotes and colons.
2. It's common to use dicts as configuration, this dicts may be very similar differing only
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


MyOtherDict.as_dict()  # return a dynamically create dict
```
