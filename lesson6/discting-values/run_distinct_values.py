from discting_values import solution


file_name = input()
with open(file_name) as f:
    content = f.read().strip()
    a = list(map(int, content.split('\n')))

print(solution(a))
