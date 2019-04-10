def solution(a, k):
    if len(a) == 0:
        return a
    k = k % len(a)
    return a[-k:] + a[:-k]
