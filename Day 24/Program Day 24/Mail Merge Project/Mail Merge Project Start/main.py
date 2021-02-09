# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp

# initializing constants
START_LETTER_PATH = "./Input/Letters/starting_letter.txt"
INVITED_NAME_PATH = "./Input/Names/invited_names.txt"
NAME = "[name]"

# opening file starting_letter.txt in read mode
with open(START_LETTER_PATH) as main_letter:
    letter_content = main_letter.read()

# opening file invited_names.txt in read mode
with open(INVITED_NAME_PATH) as name_list:

    # reading the contents in the file invited_name.txt line by line and storing each lines in a list
    name_list = name_list.readlines()

for name in name_list:

    # striping each names in name_list so that the name can be written without next nextline
    new_name = name.strip()

    # path for the place the final file to be stored
    READY_TO_SEND_PATH = f"./Output/ReadyToSend/send_to_{new_name}.txt"

    # replacing the name in file
    new_letter = letter_content.replace(NAME, new_name)

    # opening the resultant file in write mode to create the final file
    with open(READY_TO_SEND_PATH, mode="w") as ready:
        ready.write(new_letter)



