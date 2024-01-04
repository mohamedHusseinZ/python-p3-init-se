#!/usr/bin/env python3

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old.")
my_dog.bark()
