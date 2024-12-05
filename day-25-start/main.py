# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

"""using csv module"""
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         # print(row)
#         try:
#             temperature.append(int(row[1]))
#         except ValueError:
#             pass
#     print(temperature)


"""using pandas module"""
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


"""converting data into dictionary"""
data_dict = data.to_dict()
print(data_dict)


"""converting data into list"""
temp_list = data["temp"].to_list()
# calculation of average
average = sum(temp_list) / len(temp_list)
rounded_average = round(average, 2)
print(rounded_average)
# calculate average with panda
print(round(data["temp"].mean(), 2))

"""calculation with pandas model"""
print(data["temp"].max())

"""calling data in a row"""
print(data[data.temp == data.temp.max()])

"""pulling out single condition in row"""
monday = data[data.day == "Monday"]
conv = monday.temp * 9/5 + 32
print(conv)
# -- sunny -- #

"""conv dictionaries in to pandas DataFrame"""
data_dict = {
    "names": ["mike", "nancy", "nike"],
    "scores": [12, 23, 34,]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_csv.csv")