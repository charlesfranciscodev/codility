from collections import defaultdict


def solution(dna_sequence, p, q):
    letters = "ACGT"
    impact_factor = {letter:i+1 for i, letter in enumerate(letters)}
    answer = []
    first_prefix_sum = defaultdict(int)
    first_prefix_sum[dna_sequence[0]] = 1
    # dna_sequence_index => prefix sum for each letter
    prefix_sums = [first_prefix_sum]

    # compute prefix sums
    for index in range(1, len(dna_sequence)):
        letter = dna_sequence[index]
        prefix_sum = {}
        for key in impact_factor.keys():
            prefix_sum[key] = prefix_sums[index - 1][key]
        prefix_sum[letter] += 1
        prefix_sums.append(prefix_sum)

    # compute answer
    for i, j in zip(p, q):
        for key in impact_factor.keys():
            previous_prefix_sum = 0
            if i > 0:
                previous_prefix_sum = prefix_sums[i - 1][key]
            if prefix_sums[j][key] - previous_prefix_sum > 0:
                answer.append(impact_factor[key])
                break
    
    return answer
