
# using normal function , here we get the data in a format which is very hard to process and need extra work to be done.
print("using normal method")
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
for row in data:
    data_stripped = row.strip()
    final_data = [data_stripped]
    print(final_data)              # it still needs more work even after this for better usage


# ********************************************************************************
print("****************************************************************************")
# ********************************************************************************


# using csv library we get csv data which can be easy to process
import csv
print("using csv library")
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
print(temperature)
# even if csv module make csv file easy to work with ,it' still is not very easy to work with large size data.


# **********************************************************************************
print("********************************************************************************")
# **********************************************************************************


# using pandas library ,its very easy to read csv and other data's in pandas
print("using pandas library")
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
