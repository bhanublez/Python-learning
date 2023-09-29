#Exporating data analysis (EDA)
#Not possible to get without matplotlit

#How to deal with missing values
import pandas as pd
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??',"????"])
cars_data.head(10)
#Deep copy of data not shallow copy
cars_data2=cars_data.copy()
cars_data2.info()
cars_data2.isna().sum()
cars_data2.describe()

print(cars_data2['Age'].mean())
cars_data2['Age'].fillna(cars_data2['Age'].mean(),inplace=True)
# print(cars_data2.isna().sum())

#count Value function
# print(cars_data2['FuelType'].value_counts().index[0])
# print(type(cars_data2['FuelType'].value_counts()))



# print(cars_data2.info())
# cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0],inplace=True)
# print(cars_data2)



#FUELTYPE preprocessing
print(type(cars_data2['FuelType'].value_counts()))
cars_data2['FuelType'].value_counts().index[0]
cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0],inplace=True)



#MET COLOR preprocessing
cars_data2['MetColor'].fillna(cars_data2['MetColor'].mean(),inplace=True)
print(cars_data2.isna().sum())

print(cars_data2.info())



#KM preprocessing
# cars_data2.isna().sum()
cars_data2['KM'].fillna(cars_data2['KM'].mean(),inplace=True)
print(cars_data2.isna().sum())

print(cars_data2.info())
cars_data3=cars_data
cars_data3=cars_data3.apply(lambda x:x.fillna(x.mean) if x.dtype=='float' else x.fillnan(x.value_counts().index[0]))



