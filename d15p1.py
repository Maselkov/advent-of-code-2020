import puzzleinput

numbers = [int(x) for x in puzzleinput.lines[0].split(",")]
last = None
for i in range(2020 - len(numbers)):
    last = numbers[-1]
    if numbers.count(last) == 1:
        numbers.append(0)
    else:
        t = list(reversed(numbers[:-1])).index(last) + 1
        numbers.append(t)

print(numbers[-1])
