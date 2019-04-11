def solution(a):
    occurences = set()
    for x in a:
        occurences.add(x)
    i = 1
    while True:
        if i not in occurences:
            return i
        i += 1
