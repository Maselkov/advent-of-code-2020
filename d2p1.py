from os import path

valid_count = 0
with open(f"{path.basename(__file__)[:2]}.txt") as f:
    for line in f.readlines():
        string = line.split(" ")
        min_occurances, max_occurances = (int(x) for x in string[0].split("-"))
        letter = string[1][0]
        password = string[2]
        if min_occurances <= password.count(letter) <= max_occurances:
            valid_count += 1

print(valid_count)
