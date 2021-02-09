
# Absolute file path - here path is decided from the root of the computer. (eg: G:)

path = "/100 Days of code - The complete Python bootcamb/Day 22/Program Day 22/Day 22 project pong game/pong game steps.txt"
file = open(path)
read = file.read()
print(read)
file.close()


# Relative file path - here path is decided from the current working directory.

path = "../../../Day 22/Program Day 22/Day 22 project pong game/pong game steps.txt"
file1 = open(path)
read = file1.read()
print(read)
file1.close()
