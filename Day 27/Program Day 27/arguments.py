# while creating a function or class we can give default arguments

def name(first_name, last_name, middle_name=""):
    return f"{first_name} {middle_name} {last_name}"


print(name("Gopika", "P"))
print(name("Gokul", "P", "Dev"))


# *agr can be given as argument for function or class for giving multiple arguments(unlimited arguments)
# here the arguments are stored as tuple
def add(*numbers):
    result = 0
    for num in numbers:
        result += num
    print(result)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# **kwarg can be given as argument for giving unlimited keyword arguments
# here the arguments are stored as dict
def calculate(num1, **num2):
    print(num1 + num2["add"])
    print(num1 * num2["mul"])
    print(num1 - num2["sub"])


calculate(10, add=45, mul=10, sub=5)


# we can use get() along with keyword in **kwargs so to make the argument optional
class Student:
    def __init__(self, **data):
        self.name = data["name"]
        self.gender = data["gender"]
        self.p_mark = data.get("p")
        self.c_mark = data.get("c")
        self.b_mark = data.get("b")
        self.m_mark = data.get("m")
        print(data)

    def dataset(self):
        data_dict = {
            "name": self.name,
            "gender": self.gender,
            "physics": self.p_mark,
            "chemistry": self.c_mark,
            "biology": self.b_mark,
            "mathematics": self.m_mark
        }
        return data_dict


gokul = Student(name="Gokul Dev.P", gender="male", p=183, c=170, m=168)
print(gokul.dataset())
