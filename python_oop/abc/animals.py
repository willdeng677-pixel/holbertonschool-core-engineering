#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Create objects
dog = Dog()
cat = Cat()

# Display the sounds
print(dog.sound())
print(cat.sound())
