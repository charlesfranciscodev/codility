def solution(n, a):
    counters = []
    max_counter = 0
    prev_max_counter = 0

    for i in range(1, n + 1):
        counters.append(0)

    for number in a:
        if number == n + 1:
            prev_max_counter = max_counter
        else:
            counters[number - 1] = max(counters[number - 1], prev_max_counter) + 1
            max_counter = max(max_counter, counters[number - 1])

    for i in range(0, n):
        counters[i] = max(counters[i], prev_max_counter)
    
    return counters
