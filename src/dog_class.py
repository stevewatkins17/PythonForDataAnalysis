# this example is adapted from "Python Crash Course" by Eric Mathes
class Dog:
    def __init__(self ,name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

