#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    unique_numbers = set()

    for i in my_list:
        if i not in unique_numbers:
            total += i
            unique_numbers.add(i)
    return (total)
