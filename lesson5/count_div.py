def solution(a, b, k):
    start = ((a + k - 1) // k) * k
    return (b - start) // k + 1
