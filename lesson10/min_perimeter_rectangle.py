import math


def divisors(n):
    a = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            a.append((i, n // i))
        i += 1
    return a


def solution(n):
    min_perimeter = math.inf
    for x, y in divisors(n):
        perimeter = (x + y) * 2
        min_perimeter = min(min_perimeter, perimeter)
    return min_perimeter
