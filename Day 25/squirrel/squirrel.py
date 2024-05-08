import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240508.csv")

gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")