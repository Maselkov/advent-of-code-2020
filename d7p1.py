import puzzleinput

lines = puzzleinput.lines

bags = {}
for line in lines:
    line = line.replace(", ", " ").replace(".", "").replace("contain", "")
    line = line.replace("bags", "bag").split(("bag"))
    line = [item.strip() for item in line if item]
    bag_color = line[0]
    contents = {}
    if line[1] != "no other":
        for item in line[1:]:
            count, color = item.split(" ", 1)
            contents[color] = int(count)
    bags[bag_color] = contents


def can_contain(bag, target):
    for sub_bag in bag:
        if sub_bag == target:
            return True
        else:
            if can_contain(bags[sub_bag], target):
                return True
    return False


bag_count = 0
for bag in bags.values():
    if can_contain(bag, "shiny gold"):
        bag_count += 1
print(bag_count)
