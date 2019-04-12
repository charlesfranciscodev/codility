def is_valid_triplet(t):
    P, Q, R = 0, 1, 2
    return  t[P] + t[Q] > t[R]


def solution(a):
    a.sort()
    for i in range(0, len(a) - 3 + 1):
        triplet = a[i:i+3]
        if is_valid_triplet(triplet):
            return 1
    return 0
