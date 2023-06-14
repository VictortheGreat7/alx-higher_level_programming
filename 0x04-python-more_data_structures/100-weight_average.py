#!/usr/bin/python3

def weight_average(my_list):
    if len(my_list) == 0:
        return (0)

    total_score = 0
    total_weight = 0

    for tuple in my_list:
        score = tuple[0]
        weight = tuple[1]

        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return (0)

    weighted_average = total_score / total_weight
    return (weighted_average)
