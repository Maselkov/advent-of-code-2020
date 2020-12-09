import puzzleinput
numbers = puzzleinput.numbers

for i, n in enumerate(numbers):
    sought = 2020 - n
    if sought in numbers[i:]:
        print(sought * n)
