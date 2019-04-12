from collections import Counter


def solution(a):
    counter = Counter()
    for value in a:
        counter[value] += 1
    half_length = len(a) // 2
    for value, count in counter.items():
        if count > half_length:
            return a.index(value)
    return -1
