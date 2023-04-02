import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
count_list = [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

# count = data["Primary Fur Color"].value_counts()
# count_list = count.to_list()

fur_colors_dict = {
    "Fur Color" : ["Grey", "Red", "Black"],
    "Count" : count_list
}

df_squirrel_count = pandas.DataFrame(fur_colors_dict)
df_squirrel_count.to_csv("squirrel_count.csv")