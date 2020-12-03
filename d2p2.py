import puzzleinput

valid_count = 0
for line in puzzleinput.lines:
    string = line.split(" ")
    letter = string[1][0]
    password = string[2]
    matches = 0
    for pos in (int(x) - 1 for x in string[0].split("-")):
        if password[pos] == letter:
            matches += 1
    if matches == 1:
        valid_count += 1

print(valid_count)
