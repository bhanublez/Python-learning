# Regular Expression

It also refer as regex and refexp.  
It search query for searching a string pattern from provided string or content.     
It allows us to search a text for specific pattern.
We can use it whole amount of languages.

### Basic Example

```python
data="August 23 07:59:23 my friend farted in class room, we viral his video on this number [12345]"
index=data.index('[')

# Normal Way which uses internally  complex process
print(data[index+1:index+6])

#Now regular expression method
import re
regex= r"\[(\d+)\]"
result=re.search(regex,data)
print(result[1])
# print(grep thron )
```
## Dot Expression

A dot(.) matches any character. 
Also referred as WILDCARD
```python
str="Hello every my name is anam amam adam"
print(re.findall(r"\b[aA]\w+",str))
print(re.findall(r"a.am",str))
print(re.search(r"p.ng","Sponge",re.IGNORECASE))
#output: <re.Match object; span=(1, 5), match='pong'>
```
```
Always  use raw string for regular expression in Python
```
```python
import regex
result=re.search(r"aza","Plaza")
print(result)
# Output:  <re.Match object; span=(2, 5), match='aza'>
result=re.search(r"aza","bazaar")
print(result)
# Output: <re.Match object; span=(1, 4), match='aza'>

# In case if data is not available then
print(re.search(r"aza","Bleza"))
#Output: None (it mean it did'nt find the match)

```

## Start and End line Expression Symbol

### Start represented by (^) 
```python
import re

print(re.search(r"^x","xenon"))
#<re.Match object; span=(0, 1), match='x'>

```
### End Expression ($)

```python 
print(re.search("ple$","apple diple rinkle single"))
```
## Uper And lower Case Handling
```python
print(re.search(r"[Pp]ython","python"))
print(re.search(r"[a-z]way","The end of life cycle"))
print(re.findall("dance[\s\w]","the dancer are rocking the room, there dancing skill is of next level and dance4 dance* are special move"))

# pipeline can be used to separate multiple search condition in regex expression
print(re.findall(r"cat|dog","Cats and Dogs are shitting on the streets, strict action needed on both cats and dogs",re.IGNORECASE))

#using * expression we increase length of character from 0 to many
print(re.search(r"Py.*n","Pynononononp"))
print(re.findall(r"Py[a-z]*n","Python Py123on Py**on Pyon"))

#In case of + 1 or more
print(re.findall(r"Py[a-z]+n","Python Py123on Py**on Pyon"))
#In case of ? 1 or 0
print(re.findall(r"Py[a-z]?n","Python Py123on Py**on Pyon"))

```

## Escape Sequence
```python
# \ character example
print(re.search(r".com","welcome"))
print(re.search(r"\.com","welcome"))
print(re.search(r"\.com","google.com"))
# w character example mean all none space character
print(re.search(r"\w*","This is an example of shit"))
print(re.search(r"\w*","This-is_an_example_of_shit"))
```

```
\d Matches any decimal digit [0-9]
\D Matches non decimal digit [^0-9]
\s Matches white space character [\t\n\r\f\v]
\S Matches non white space character
\w matches Alphanumeric value [a-zA-Z0-9_]
\W non alphanumeric value
```

## Special Methods

1. match() determine re matches at beginning of string
2. search() scan through string looking form match in RE
3. findall() scan through the string to return all matched string and return them in list format
4. finditer() here return matched substring as iterator

### other supporting function and attributes

a. group() return the string matched by RE
b. start() return the starting position og match
c. end() return the ending position of matched
d. span() return a tuple containing start and position of the match 

## Capturing groups

Portion of the pattern that are enclosed in parentheses
```python
import re
result=re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[1],result[2]))

def rearrange_name(name):
    result=re.search(r"^([\w\.\-]*), ([\w\.\-]*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
print(rearrange_name("-Ama-za, da.nza, canz.a"))

```

## Repetition Qualifiers

```python
import re
print(re.search(r"[a-zA-Z]{5}","a ghost"))
print(re.search(r"[a-zA-Z]{5}","a scary ugly ghost run behind a person to fart on his or her face"))
print(re.findall(r"[a-zA-Z]{5}","a scary ugly ghost run behind a person to fart on his or her face"))

## use of \b to search at fixed mentioned length
print(re.findall(r"\b[a-zA-Z]{5}\b",'A scary ghost farts'))
#Allocating range 
print(re.findall(r"\w{5,10}","I really hate going my college as its to boring"))

print(re.findall(r"s\w{,20}","I loves strawberrieses"))
```

### Extracting Process Id

```python
import re
def extract_pid(log_line):
    regex=r"\[(\d+)]"
    result=re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid("Something want wrong in process fork whose id is [29247]"))
print(extract_pid("Something want wrong in process fork whose id is [afbjb]"))# return empty string
```

## Split Function in regular expression

````python
import re
print(re.split(r"[.?!]","One sentence. Another sentence? and last one!"))


print(re.split(r"([.?!])","One sentence. Another sentence? and last one!"))
``````