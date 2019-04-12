def solution(a):
    current_sum = max_sum = -1000000
    for value in a:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)
    return max_sum
