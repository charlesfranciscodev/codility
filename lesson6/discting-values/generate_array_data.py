import random

file_name = input()

with open(file_name, "w") as f:
    for i in range(0, 10 ** 6):
        random_number = random.randint(1, 10 ** 9)
        f.write(str(random_number) + '\n')
