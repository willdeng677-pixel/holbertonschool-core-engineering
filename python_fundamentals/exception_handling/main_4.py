#!/usr/bin/env python3

safe_print_list_integers = __import__('4-print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, "School", "Python"]

nb_print = safe_print_list_integers(my_list, 6)
print("nb_print: {:d}".format(nb_print))
