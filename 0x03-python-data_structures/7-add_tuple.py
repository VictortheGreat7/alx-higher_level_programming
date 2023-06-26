#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_tuple = tuple_a + (0, 0)
    b_tuple = tuple_b + (0, 0)
    c_tuple = (a_tuple[0] + b_tuple[0], a_tuple[1] + b_tuple[1])
    return (c_tuple)
