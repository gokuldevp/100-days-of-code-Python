# try is used to give the thing we need as input.

try:

    total = 123 - "123"
# except is used do operation if we catch an error during try.
# the problem is that even if its one or more error the except will except will execute.
# so for multiple exception it is good to specify the exception
except:
    print("there is an error")

# *********************************************************************************************************************
# so for multiple exception it is good to specify the exception and specify what to do with them
# we can also use the as function to get the statement of the exception
# else is used to to operations when the try block didn't find any exception
# finally is executed if exception is found/not found on in try block


num1 = 198
num2 = "123"
try:
    file = open("abc.txt")
    # dict_1 = {
            # "key": "value"
        # }
    # print(dict_1["hi"])
    total = num1 + num2
except TypeError as type_error:
    print(f"there is a type error -> {type_error}.")
except FileNotFoundError as file_error:
    print(f"There is a error at {file_error}")
    file = open("abc.txt", "w")
    file.write("hi there")
else:
    print("there is no error")
finally:
    file.close()
# **********************************************************************************************************************

# for raise exception we use raise

height = int(input("Enter the height in cm: "))
weight = int(input("Enter the weight in kg: "))
bmi = weight/(height/100)**2
if height > 400:
    raise ValueError("check your height again")

else:
    print(f"{bmi:.2f}")
