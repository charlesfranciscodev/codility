def solution(a):
    value_set = set()
    total = 0
    for value in a:
        if value not in value_set:
            value_set.add(value)
            total += 1
    return total
