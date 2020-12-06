import puzzleinput

lines = puzzleinput.lines

answered = []
groups = []
for line in lines:
    if not line:
        groups.append(answered)
        answered = []
        continue
    for letter in line:
        if letter not in answered:
            answered.append(letter)
groups.append(answered)
print(sum(len(x) for x in groups))
