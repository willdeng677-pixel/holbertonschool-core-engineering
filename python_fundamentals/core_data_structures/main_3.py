#!/usr/bin/env python3

element_at = __import__('element_at').element_at

list = [1, 2, 3, 4, 5]
index = 3
print("Element at index {:d} is {}".format(index, element_at(list, index)))
