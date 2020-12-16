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

valid_tickets = tickets[:]
for ticket in tickets:
    for value in ticket:
        for rule in rules.values():
            if validate(value, rule):
                break
        else:
            valid_tickets.remove(ticket)
            break

options = []
for i in range(len(my_ticket)):
    valid_options = list(rules)
    for ticket in valid_tickets:
        for name, rule in rules.items():
            if not validate(ticket[i], rule):
                if name in valid_options:
                    valid_options.remove(name)
    options.append(valid_options)

guaranteed = {}
to_remove = None
while len(guaranteed) != len(rules):
    for i, values in enumerate(options):
        if to_remove in values:
            values.remove(to_remove)
            options[i] = values
            continue
        if len(values) == 1:
            guaranteed[i] = values[0]
            to_remove = values[0]
result = 1
for index, value in guaranteed.items():
    if value.startswith("departure "):
        result *= my_ticket[index]
print(result)
