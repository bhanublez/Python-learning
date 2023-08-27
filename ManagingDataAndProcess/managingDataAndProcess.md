# IO streams

The basic mechanism for performing input and output operation in your program

1. standard input (STDIN)
2. standard output (STDOUT)
3. standard error (STDERR)

## Shell

A command-line interface used to interact with your operating system.  
In Linux Bash is refer as shell.  
Python program get executed inside a shell command line environment. 
The variable set in that environment are another source of information that we can use in our scripts.
Ti check in linux type 'env'. Also path line "echo $Path"
```python
import os
print("HOME: "+os.environ.get("HOME",""))
```
