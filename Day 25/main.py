# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatues = []
#
#     for row in weather_file:
#         getting_temperatue = row.split(",")
#
#         if getting_temperatue[1] != "temp":
#             temperatues.append(int(getting_temperatue[1]))

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

average_pandas = data['temp'].mean()
max_pandas = data['temp'].max()
average = sum(temp_list)/len(temp_list)

print(average, average_pandas, max_pandas)

# Get data in columns
print(data.condition)

#Get data in row
print(data[data['day'] == "Monday"])

print(data[data['temp'] == data['temp'].max()])

monday = data[data['day'] == "Monday"]
print((monday['temp']*9/5)+32)




