# with open("weather_data.csv") as file:
# 	data = file.readlines()
# 	print(data)


# import csv

# with open("weather_data.csv") as file:
# 	data = csv.reader(file)
# 	print(data)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
# print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_data = data["temp"].to_list()


# print(f"Temperature average: {round(sum(temp_data) / len(temp_data),2)}")
# print(f"Max temperature: {max(temp_data)}")

# high_temp = data[data.temp == data.temp.max()]
# print(data)
# monday = data[data.day == "Monday"]

# print(f"f{(monday.temp[0]*9/5)+32}")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df = data["Primary Fur Color"].value_counts()
df.to_csv("squirrel_count.csv")
print(df)