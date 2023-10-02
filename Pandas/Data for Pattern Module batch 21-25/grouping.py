import pandas as pd
df=pd.read_csv('weather_data_cities.csv')

india_weather=pd.DataFrame({"city":['hamda','banglore','pune'],'tempeature':[33,45,45],'humidity':[80,60,75]})
# print(india_weather)

TumTum_weather=pd.DataFrame({"city":['dangle','manglo','london'],'tempeature':[33,45,45],'humidity':[80,60,75]})
# print(TumTum_weather)

df=pd.concat([india_weather,TumTum_weather],ignore_index=True,sort=True)

print(df)

# pajama=pd.DataFrame({"Pajama":['long','short','transparent'],'size':[33,45,45],'humidity':[80,60,75]})

# df=pd.concat([india_weather,pajama],ignore_index=True)
# print(df)


firt_temp=pd.DataFrame({"city":['hamda','banglore','punda'],'tempeature':[33,45,45]})
second_temp=pd.DataFrame({"city":['hamda','banglore','dunda'],'humidity':[80,60,75]})
print(second_temp)
#natural join
df=pd.merge(firt_temp,second_temp,on="city")
print(df)
#left join 

df=pd.merge(firt_temp,second_temp,on="city",how='left')
print(df)

