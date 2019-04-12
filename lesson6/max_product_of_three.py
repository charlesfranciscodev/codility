import math


def solution(a):
    # sort
    a.sort()
    # test top 3 positive values
    product1 = a[-1] * a[-2] * a[-3]
    # test bottom 2 values with top positive value
    product2 = a[0] * a[1] * a[-1]
    return max(product1, product2)
