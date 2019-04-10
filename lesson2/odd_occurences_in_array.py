def solution(a):
    s = set()
    for n in a:
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    return s.pop()
