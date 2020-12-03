import puzzleinput

valid_count = 0
for line in puzzleinput.lines:
    string = line.split(" ")
    min_occurances, max_occurances = (int(x) for x in string[0].split("-"))
    letter = string[1][0]
    password = string[2]
    if min_occurances <= password.count(letter) <= max_occurances:
        valid_count += 1

print(valid_count)
