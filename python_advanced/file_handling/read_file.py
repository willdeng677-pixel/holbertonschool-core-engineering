#!/usr/bin/env python3

# Function that reads text file and print its contents

def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end"")
