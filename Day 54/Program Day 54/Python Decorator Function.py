from time import sleep


def decorator_function(function):

    def wrapper_function():

        sleep(3)
        function()

    return wrapper_function


@decorator_function
def say_hello():
    print("Hello")


@decorator_function
def say_bye():
    print("Bye")


def good_bye():
    print("good bye")


say_bye()
good_bye()
say_hello()

good = decorator_function(good_bye)
good()
