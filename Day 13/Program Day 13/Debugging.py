############DEBUGGING#####################

# # Describe Problem
# def my_function():
#     """Here in i in range of 1 to 20 so i don't include 20 and only include upto 19 so that we dont get any out put """
#     for i in range(1, 20):
#         if i == 20:
#           print("You got it")
# my_function()


#after fixing
def my_function_1():
    for i  in range(1,21):
        if i == 20:
            print("You got it")
my_function_1()


# # Reproduce the Bug

# """here randint gives a  number from 1 to 6 
#and we use this number on list dice imgs to get
# the output but in dice imgs total elements is only 
# 6 so we need to give a number from 0 to 5. since 
#last number is stored as 1 minus total number of
# elements"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# after fixing
from random import randint
dice_imgs = ["1", "2", "3", "4","5","6"]
dice_num = randint(1,6)
print(dice_imgs[dice_num-1])

# # Play Computer
# """Here year of birth when it is 1994 have no answer"""
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# atter fixing  
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z")    



# # Fix the Errors
# """There are 3 error here print should be intented and
# there should be f before the string in print to
# get value of age also age should be an int value"""
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


# after fixing 
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}")


# #Print is Your Friend
# """there are == for word_per_page ,  it should be ="""
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# after fixing
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# # #Use a Debugger
# """b_list.appende should be in for loop"""
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


# after fixing 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])