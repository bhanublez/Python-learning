#Exporating data analysis (EDA)
#Not possible to get without matplotlit

#How to deal with missing values
import pandas as pd
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=['??','???'])
# print(cars_data.head)

#Deep copy of data not shallow copy
cars_data2=cars_data.copy()

cars_data2.info()

print(cars_data2.isna())

