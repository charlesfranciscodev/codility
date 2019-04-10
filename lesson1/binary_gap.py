from itertools import groupby


def solution(n):
    binary_string = bin(n)[2:]
    groups = [list(j) for i, j in groupby(binary_string)]
    # remove first and last groups
    groups = groups[1:len(groups) - 1]
    groups = [a for a in groups if a[0] == '0']
    longest_binary_gap = 0
    if len(groups) > 0:
        longest_binary_gap = max(map(len, groups))
    return longest_binary_gap
