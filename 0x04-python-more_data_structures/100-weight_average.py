#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_weights = sum(x[1] for x in my_list)
    sum_lambda = sum(list(map(lambda x: x[0] * x[1], my_list))) / total_weights
    return sum_lambda
