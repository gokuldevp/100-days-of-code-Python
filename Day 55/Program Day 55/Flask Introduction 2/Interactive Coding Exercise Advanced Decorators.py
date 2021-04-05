def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"the result : {result}")
    return wrapper


@logging_decorator
def mul_fun(a, b, c):
    return a * b * c


mul_fun(1, 2, 3)
