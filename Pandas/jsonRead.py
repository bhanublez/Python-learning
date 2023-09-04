import pandas as pd
#Uci imp
df=pd.read_csv('nyc_weather.csv')
# print(df)
#Dat available in colums
# print(df.columns)
# list=df.columns
# for i in list:
#     print(i)

#This return the data frame
# print(df.info())

#Sereis in java
#Data handling is done by Dat frame
#Data frame is collection of sereis
# print(df['EST'])
# print(type(df['EST']))

print(df['Temperature'].max())#temp

# print(df[['Temperature','EST']])
# print(df[['Temperature','EST','Events']][df["Temperature"]==df['Temperature'].max()])

print(df.describe())
print(type(df.describe()))



