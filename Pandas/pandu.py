import pandas as pd

# print(pd.__version__)
# df=pd.DataFrame()
# print(df)

# data=[['rahul',35],['bhanu',8]]
# df=pd.DataFrame(data,columns=['Name','Age'],dtype=float)
# print(df)

# data = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }

# purchases = pd.DataFrame(data)

# print(purchases)

data={
    'Name':["Riku",'Diku',"Jitu"],
    'Age':[12,1,21]
    }
student=pd.DataFrame(data)
print(student)

data=[{'a':1,'c':'Anmol','b':4},{'a':3,'c':4564,'a':45,'b':15}]
df=pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['aa', 'bb'])