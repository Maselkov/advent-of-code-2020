import puzzleinput

lines = puzzleinput.lines
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
passport = {}
passports = []
for line in lines:
    if not line:
        passports.append(passport)
        passport = {}
        continue
    for pair in line.split(" "):
        key, value = pair.split(":")
        passport[key] = value
passports.append(passport)
valid_passports = 0
for passport in passports:
    for key in required_fields:
        if key not in passport:
            break
    else:
        valid_passports += 1
print(valid_passports)
