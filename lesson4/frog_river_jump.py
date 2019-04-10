def solution(x, a):
    positions = set()
    for position in range(1, x + 1):
        positions.add(position)
    for i, leaf_position in enumerate(a):
        positions.discard(leaf_position)
        if len(positions) == 0:
            return i
    return -1
