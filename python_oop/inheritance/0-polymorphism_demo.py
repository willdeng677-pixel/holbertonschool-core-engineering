#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
