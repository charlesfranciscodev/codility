import math


def solution(a):
    n =  len(a)
    min_difference = math.inf
    sum_head = 0
    sum_tail = sum(a)
    for i in range(0, n - 1):
        sum_head += a[i]
        sum_tail -= a[i]
        difference = abs(sum_head - sum_tail)
        min_difference =  min(min_difference, difference)
    return min_difference
