import puzzleinput

numbers = [int(x) for x in puzzleinput.lines[0].split(",")]
d = {}
for i, num in enumerate(numbers):
    d[num] = i + 1
next_number = 0
for i in range(len(numbers) + 1, 30000000):
    if next_number in d:
        age = i - d[next_number]
    else:
        age = 0
    d[next_number] = i
    next_number = age
    if i == 30000000 - 1:
        print(age)
