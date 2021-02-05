# Class Inheritance

class Animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("breath air in and breath air out.")

    def move(self):
        print("moves very well")


class Fish(Animal):
    """the class inherited its features from class Animal"""
    def __init__(self):
        super().__init__()

    def swim(self):
        super().move()
        print("in the water.")


dodo = Fish()
dodo.breath()
dodo.swim()
print(dodo.eyes)

# Slice works in list and tuple

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lists[1:8:2])
print(lists[0:5])
print(lists[1:])

