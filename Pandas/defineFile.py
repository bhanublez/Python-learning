import pandas as pd
#Al three mention below are source data 
#(Here data stor in time based manner)
# 1. PDA->personal digital assistant
# 2. Pc and 3. Mobile app

#ETL->Extact tranform and  load

df=pd.read_csv('nyc_weather.csv')
# print(df)
# print(df.to_csv('bhanu.csv',index=False))
# print(df.to_excel("amol.xml",sheet_name="anmol_data",index=False))

# g=df.groupby('city')
# r=pd.DataFrame(g)
# print(r)

g=df.groupby('city')
for city,city_dataframe in g:
    print(city)
    print("data frame of individual city")
    print(city_dataframe)

