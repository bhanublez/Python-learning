# Module

Is a collection of functions and variables that are grouped together in a single file (called module) for reuse in other programs.

A package is a directory that contains collections of modules; it has an __init__.
py file, which lets the interpreter know that it is a package.

## Module aliasing or renaming

It is possible to rename a module when importing it, using the 'as' keyword.
Another method using the 'from' keyword is also possible.

```python
import math as m
from math import sqrt as s
``````

## Special variables

#### __name__ : name of the module

    1."This data is only available when the module is run directly, not when it is imported."
    2. "If Program is execute individually then __name__ = __main__"
    3. "If Program is imported then __name__ = module name"

## Types of Files

    1. Text files (.txt)
    2. Binary files (.bin)
    3. CSV files (.csv)
    4. JSON files (.json)
    5. XML files (.xml)
    6. HTML files (.html)
    7. Image files (.jpg, .png, .gif, .bmp, .svg)
    8. Audio files (.mp3, .wav, .ogg, .mp4)

# File Handling

f=open("File name","mode ")

## mode

    1. r - read mode
    2. w - write mode
    3. a - append mode
    4. r+ - read and write mode
    5. w+ - write and read mode
    6. a+ - append and read mode

## Status of file
```python
file=open("anmol.txt",'r+')
print(file.readlines())
print("file name",file.name)
print("file mode",file.mode)
print("file readable ",file.readable())
print("file writeable ",file.writable())
print("file is close ",file.closed)
print("file is close now ",file.closed)
```


## readable methods
```python
# readable methods
print(file.read())# read() method read whole file
print(file.tell())# tell() method tells the current position of the file pointer
print(file.read(5))# read(n) method read n characters from the file
print(file.readline(144))# readline() method read one line from the file
print(file.readlines())# readlines() method read all lines from the file and return a list of lines
print(file.seek(0))# seek() method change the current position of the file pointer
print(file.seek(0,2))# seek(offset,from) method change the current position of the file pointer
print(file.seekable())# seekable() method check whether the file is seekable or not
```
