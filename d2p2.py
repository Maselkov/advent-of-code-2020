from os import path

valid_count = 0
with open(f"{path.basename(__file__)[:2]}.txt") as f:
    for line in f.readlines():
        string = line.split(" ")
        positions = [int(x) - 1 for x in string[0].split("-")]
        letter = string[1][0]
        password = string[2]
        matches = 0
        for pos in positions:
            if password[pos] == letter:
                matches += 1
        if matches == 1:
            valid_count += 1

print(valid_count)
