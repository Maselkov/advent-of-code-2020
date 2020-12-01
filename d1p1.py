from os import path
with open(f"{path.basename(__file__)[:2]}.txt") as f:
    numbers = [int(x) for x in f.readlines()]

for i, n in enumerate(numbers):
    sought = 2020 - n
    if sought in numbers[i:]:
        print(sought * n)
