import puzzleinput

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate_passport(passport):
    for key in required_fields:
        if key not in passport:
            return False
    for key, value in passport.items():
        if key == "byr":
            if not value.isnumeric() or len(value) != 4:
                return False
            value = int(value)
            if not 1920 <= value <= 2002:
                return False
        elif key == "iyr":
            if not value.isnumeric() or len(value) != 4:
                return False
            value = int(value)
            if not 2010 <= value <= 2020:
                return False
        elif key == "eyr":
            if not value.isnumeric() or len(value) != 4:
                return False
            value = int(value)
            if not 2020 <= value <= 2030:
                return False
        elif key == "hgt":
            unit = "".join([c for c in value if c.isalpha()])
            if not unit:
                return False
            measurement = int(value.replace(unit, ""))
            if unit == "cm":
                if not 150 <= measurement <= 193:
                    return False
            if unit == "in":
                if not 59 <= measurement <= 76:
                    return False
        elif key == "hcl":
            if not value.startswith("#") or len(value) != 7:
                return False
            for c in value:
                if ord("0") > ord(c) > ord("f"):
                    return False
        elif key == "ecl":
            valid_values = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
            if value not in valid_values:
                return False
        elif key == "pid":
            if len(value) != 9:
                return False
            for c in value:
                if not c.isdigit():
                    return False
        passport[key] = value
    return passport


lines = puzzleinput.lines
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
    if validate_passport(passport):
        valid_passports += 1
print(valid_passports)
