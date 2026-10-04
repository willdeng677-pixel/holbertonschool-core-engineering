#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Create a Dragon object
dragon = Dragon()

# Demonstrate the Dragon's abilities
dragon.swim()
dragon.fly()
dragon.roar()
