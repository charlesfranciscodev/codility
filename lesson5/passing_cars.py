def solution(a):
    # sum of prefix sums starting from each zero value in the list
    answer = 0
    previous_sum = 0
    prefix_sum = 0
    for i in range(len(a) - 1, -1, -1):
        prefix_sum += a[i]
        if a[i] == 0:
            answer += prefix_sum
            if answer > 10 ** 9:
                return -1
    return answer
