# importing pandas library as pd
import pandas as pd

# getting and reading file path using panda function read_csv
PATH = "Squirrel_Data.csv"
SQUIRREL_DF = pd.read_csv(PATH)

# getting fur color sequence
FUR_COLOR_SER = SQUIRREL_DF["Primary Fur Color"]

# filtering out the unique colors
FUR_COLORS = FUR_COLOR_SER.unique()
count_list = []

# using for loop to count the number of squirrel of each color
for color in FUR_COLORS[1:4]:
    count = len(SQUIRREL_DF[FUR_COLOR_SER == color])
    count_list.append(count)

# adding the data into a directory
squirrel_dict = {
    "Fur Color": FUR_COLORS[1:4],
    "Count": count_list
}

# creating data frame and convert the directory into csv file
df = pd.DataFrame(squirrel_dict)
df.to_csv("Squirrel count.csv")
