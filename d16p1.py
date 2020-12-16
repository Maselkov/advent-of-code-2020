import puzzleinput


def get_ranges(line):
    ranges = []
    for r in line.split(" or "):
        ranges.append(tuple(int(x) for x in r.split("-")))
    return ranges


def get_ticket(line):
    return [int(x) for x in line.split(",")]


def validate(value, rule):
    for lower, upper in rule:
        if lower <= value <= upper:
            return True
    return False


rules = {}
my_ticket = []
tickets = []
empty_count = 0
for line in puzzleinput.lines:
    if not line:
        empty_count += 1
        continue
    if not empty_count:
        key, value = line.split(": ")
        rules[key] = get_ranges(value)
        continue
    if "ticket" in line:
        continue
    if empty_count == 1:
        my_ticket = get_ticket(line)
    else:
        tickets.append(get_ticket(line))

error_rate = 0
for ticket in tickets:
    for value in ticket:
        for rule in rules.values():
            if validate(value, rule):
                break
        else:
            error_rate += value
print(error_rate)
