import puzzleinput

lines = puzzleinput.lines

answered = []
groups = []
new_group = True
for line in lines:
    if not line:
        groups.append(answered)
        answered = []
        new_group = True
        continue
    if new_group:
        new_group = False
        answered = set(line)
        continue
    to_remove = []
    for letter in answered:
        if letter not in line:
            to_remove.append(letter)
    for letter in to_remove:
        answered.remove(letter)
groups.append(answered)
print(sum(len(x) for x in groups))
