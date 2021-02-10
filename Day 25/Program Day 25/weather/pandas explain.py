import pandas
weather_df = pandas.read_csv("weather_data.csv")

# to check type, mainly consists of dataframe and series
print(type(weather_df))
temp_se = weather_df["temp"]
print(type(temp_se))

print("**************************************************************************")

# to change type

weather_dict = weather_df.to_dict()
print(weather_dict)
temp_list = temp_se.to_list()
print(temp_list)
print("**************************************************************************")

# # to find mean

"""normal way"""
average_temp_nor = sum(temp_list)/len(temp_list)
print(f"average temperature normally: {average_temp_nor}")
"""using pandas function"""
average_temp_pandas = temp_se.mean()
print(f"average temperature using pandas function: {average_temp_pandas}")
"""finding maximum temperature"""
max_temp = temp_se.max()
print(f"maximum temperature using pandas function: {max_temp}")
print("***************************************************************************")

# Getting hold of Columns

"""in pandas df[column_name] is same as df.column_name"""
print(weather_df["day"])
print(weather_df.day)
print("*****************************************************************************")

# Getting hold of rows

print(weather_df[weather_df.day == "Monday"])

"""to get hold of row with highest temperature"""
max_temp_row = weather_df[weather_df.temp == weather_df.temp.max()]
print(f"the row with the highest temperature is: \n{max_temp_row}")
print(f"Day with max temperature: \n{max_temp_row.day}")

"""to get monday temperature in fahrenheit."""
monday_row = weather_df[weather_df.day == "Monday"]
monday_temp_in_c = monday_row.temp
monday_temp_in_fa = (monday_temp_in_c * 9/5) + 32
print(monday_temp_in_fa)


# creating a dataframe from scratch
student_dict = {
    "name": ["arjun", "gopika", "gokul", "sanithya", "jishnu", "vishnu"],
    "mark": [90, 92, 89, 95, 93, 91]
}
student_file = pandas.DataFrame(student_dict)
print(student_file)
student_file.to_csv("student data.csv")

