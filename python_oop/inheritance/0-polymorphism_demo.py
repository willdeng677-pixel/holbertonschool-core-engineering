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


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
