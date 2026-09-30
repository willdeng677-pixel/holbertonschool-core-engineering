#!/usr/bin/env python3

alphabet = ""

for number in range(97, 123):
    letter = chr(number)
    if letter != "q" and letter != "e":
        alphabet += letter

print(alphabet)
