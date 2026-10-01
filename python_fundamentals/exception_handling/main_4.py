#!/usr/bin/env python3

safe_print_list_integers = __import__('4-print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4]

safe_print_list_integers(my_list, 4)

print(my_list[5])
