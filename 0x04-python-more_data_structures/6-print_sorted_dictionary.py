#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    def recursive_sort(dictionary):
        sorted_keys = sorted(dictionary.keys())
        for key in sorted_keys:
            value = dictionary[key]
            if isinstance(value, dict):
                print(key, ":")
                recursive_sort(value)
            else:
                print(key, ":", value)
    recursive_sort(a_dictionary)
