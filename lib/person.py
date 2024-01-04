#!/usr/bin/env python3


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
john = Person(name="John", age=30)

# Accessing attributes and calling methods
print(f"{john.name} is {john.age} years old.")
john.greet()

