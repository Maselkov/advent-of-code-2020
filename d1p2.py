import puzzleinput
numbers = puzzleinput.numbers()

for i, n in enumerate(numbers):
    for m in numbers[i:]:
        sought = 2020 - m - n
        if sought in numbers[i:]:
            print(sought * n * m)
            break
