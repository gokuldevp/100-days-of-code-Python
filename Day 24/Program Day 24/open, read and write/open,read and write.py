file = open("test.txt")                      # open is used to open a file, it is set default as read
content = file.read()
print(content)
file.close()                                 # a open file should be closed

file1 = open("test.txt", mode="w")           # 'w' is used to set it to write mode, it delete the current content
file1.write("hi there")
file1.close()

file2 = open("test.txt", mode="a")           # 'a' is used to append
file2.write("\nbye")
file2.close()

with open("test.txt", mode="a") as file3:    # is we use this format to open we don't need to close it separately
    file3.write("\nking kong")
