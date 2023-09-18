import pandas as pd

#What is use of loc and iloc
s=pd.Series(list('abcde'),index=[15,'4',1,0,4])
# print(s)

print(s.loc[15])#loc->location 
print(s.loc[0])
print(s.iloc[0])