import math


def solution(a):
    min_average = math.inf
    min_index = 0
    for i in range(2, 4):
        for j in range(0, len(a) - i + 1):
            sub_list = a[j:j+i]
            average = sum(sub_list) / len(sub_list)
            if average < min_average:
                min_average = average
                min_index = j
    return min_index
