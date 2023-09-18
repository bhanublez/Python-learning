# Data preProcessing
import numpy as np
import pandas as pd
import sklearn as skk
import seaborn as sns

#how to deal with categorical data
d={'status':['pass','fail','absent'],'marks':[100,50,80]}
studf=pd.DataFrame(data=d,columns=['status','marks'])
print(studf)

#changing categorical data using dumpy method
studf=pd.get_dummies(data=studf,prefix='s',columns=['status'])
print(studf)

#Standarization is process of making mean as zero and varaiance as one
from sklearn import datasets
iris=datasets.load_iris()
print(iris)

x=iris['data'][:,[2,3]]
y=iris['target']
print(x)
print(y)


# print(x[:,0].mean(),x[:0].std())

from sklearn import preprocessing
x_std=preprocessing.StandardScaler().fit(x)
x_s=x_std.transform(x)


# print(x[:,0].mean(),x[:0].std())

# print(x_s[:,0].mean(),x_s[:0].std())



#Normalization
#It is ration of (x-x(min)/range) where x in range of x(min) and x(max)
from sklearn import preprocessing
x_nrm=preprocessing.MinMaxScaler().fit(x)
x_n=x_nrm.transform(x)
print(x[:,0].min(),x[:,0].max())
print(x_n[:,0].min(),x_n[:,0].max())

#How to deal with missing values
