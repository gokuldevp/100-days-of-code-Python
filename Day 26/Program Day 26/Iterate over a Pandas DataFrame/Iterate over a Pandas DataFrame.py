student_dict = {
    "name": ["gokul", "dev", "p"],
    "mark": [80, 90, 70],
}

# loop in dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

df = pandas.DataFrame(student_dict)
print(df)

# looping in data frame
for (key, value) in df.items():
    print(key)
    print(value)

# looping through rows of data frame
for (index, row) in df.iterrows():
    print(index)
    print(row)
    print(row["name"])
    if row["name"] == "p":
        print(row.mark)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


