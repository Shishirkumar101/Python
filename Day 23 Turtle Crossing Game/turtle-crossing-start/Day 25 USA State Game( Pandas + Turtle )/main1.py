# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# n = data["temp"].max()
# print(data[data["temp"] == n])

# monday = data[data.day == "Monday"]
# print((monday.temp[0]*9/5) + 32)


# data_dict = {
#     "Student" : ["Shishir" , "Rohit", "Vipul"],
#     "Scores" : [76,63,61]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")



data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_Fur_color = data["Primary Fur Color"].value_counts()


grey_squirrels_count = len(data[data["Primary Fur Color"] == "Grey"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ['Gray', 'Cinnamon', 'Black'],
    "Count" : [grey_squirrels_count, red_squirrels_count , black_squirrels_count]
}

print(data_dict)

# data_dict.to_csv("new_fur_data.csv")
# data_Fur_color.to_csv("new_fur_data.csv")

fur_data = pandas.read_csv("new_fur_data.csv")
print(fur_data)