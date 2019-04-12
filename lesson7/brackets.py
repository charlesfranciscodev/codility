def is_valid(c1, c2):
    s = c1 + c2
    return s == "[]" or s == "{}" or s == "()"


def solution(s):
    stack = []
    for c in s:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            top = stack.pop()
            if not is_valid(top, c):
                return 0
    if len(stack) != 0:
        return 0
    return 1
