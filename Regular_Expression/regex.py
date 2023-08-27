import re
# data="August 23 07:59:23 my friend farted in class room, we viral his video on this number [12345]"
# index=data.index('[')

# # Normal Way which uses internally  complex process
# print(data[index+1:index+6])

# #Now regular expression method

# regex= r"\[(\d+)\]"
# result=re.search(regex,data)
# print(result[1])
# # print(grep thron )

# str="Hello every my name is anam amam adam"
# print(re.findall(r"\b[aA]\w+",str))
# print(re.findall(r"a.am",str))

# result=re.search(r"aza","Plaza")
# print(result)
# Output:  <re.Match object; span=(2, 5), match='aza'>
# result=re.search(r"aza","bazaar")
# print(result)
# Output: <re.Match object; span=(1, 4), match='aza'>

# In case if data is not available then
# print(re.search(r"aza","Bleza"))
#Output: None (it mean it did'nt find the match)

# print(re.search(r"^x","xenon"))

# print(re.search(r"p.ng","Sponge",re.IGNORECASE))

# print(re.search(r"[Pp]ython","python"))
# print(re.search(r"[a-z]cle","The end of life cycle"))
# print(re.findall("dance[\s\w]","the dancer are rocking the room, there dancing skill is of next level and dance4 dance* are special move"))

# print(re.findall(r"cat|dog","Cats and Dogs are shitting on the streets, strict action needed on both cats and dogs",re.IGNORECASE))

# print(re.search(r"Py.*n","Pynononononp"))
# print(re.search(r"a*","a asdasd"))
# print(re.findall(r"Py[a-z]*n","Python Py123on Py**on Pyon"))
# print(re.search(r".com","welcome"))
# print(re.search(r"\.com","welcome"))

# print(re.search(r"\.com","google.com"))

# print(re.search(r"\w*","This is an example of shit"))
# p=re.compile('ab*',re.IGNORECASE)
# print(p)

