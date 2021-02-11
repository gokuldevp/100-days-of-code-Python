# # list comprehension
print("****************************************************************************************\nList comprehension: ")
# new_list = [new_item for item in old_list]
old_list = [1, 2, 3, 4, 5, 6]
new_list = [(n + 1) ** 2 for n in old_list]
print(new_list)

old_string = "Gokul Dev.P"
string_list = [letter + letter for letter in old_string]
print(string_list)

# using range function
print(
    "****************************************************************************************\nusing range function: ")
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# # Conditional list comprehension
print(
    "*************************************************************************\nusing conditional list comprehension: ")
# new_list = [new_item for item in old_list if test]

names = ["king", "GOKU", "naruto", "BORUTO", "Son wukong"]
upper_list = [name.upper() for name in names if name != name.upper()]
print(upper_list)
