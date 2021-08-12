import pandas
d=pandas.read_csv("weather_data.csv")
print(type(d))
print(d)
print ("max temp=",d["temp"].max())
