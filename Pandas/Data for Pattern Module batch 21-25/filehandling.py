import pandas as pd
df=pd.read_csv('weather_data_cities.csv')
g=df.groupby('city')
for city,city_dataframe in g:
    print(city)
    print("data frame of individual city")
    print(city_dataframe)