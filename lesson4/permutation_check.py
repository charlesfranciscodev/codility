def solution(a):
    s = set()
    for x in range(1, len(a) + 1):
        s.add(x)
    for y in a:
        s.discard(y)
    return 1 if len(s) == 0 else 0
