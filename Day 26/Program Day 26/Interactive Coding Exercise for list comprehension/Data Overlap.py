# finding common numbers in both text file

file1_path = "file1.txt"
file2_path = "file2.txt"
with open(file1_path) as file1:
    file1_content = file1.readlines()
    file1_content = [int(contents.strip()) for contents in file1_content]
with open(file2_path) as file2:
    file2_content = file2.readlines()
    file2_content = [int(contents.strip()) for contents in file2_content]
result = [contents for contents in file1_content if contents in file2_content]    
# Write your code above 👆

print(result)


