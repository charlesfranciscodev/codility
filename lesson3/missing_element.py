def solution(a):
    n = len(a)
    x = (n * (n + 1) // 2) + n + 1
    for y in a:
        x -= y
    return x
