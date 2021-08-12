import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
GREY_SQUI=len(data[data["Primary Fur Color"]=="Gray"])
red_SQUI=len(data[data["Primary Fur Color"]=="Cinnamon"])
Black_SQUI=len(data[data["Primary Fur Color"]=="Black"])
print("grey=",GREY_SQUI)
print("red=",red_SQUI)
print("Black=",Black_SQUI)