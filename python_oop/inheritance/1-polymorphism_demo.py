#!/usr/bin/env python3

class Dog(Animal):
    def speak(self):
        return "Woof"

    dog = Dog()
    print(dog.speak)

class Cat(Animal):
    def speak(self):
        return "Meow"

    cat = Cat()
    print(cat.speak)
