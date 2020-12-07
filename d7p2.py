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


def get_bag_count(bag):
    total = 0
    for sub_bag, count in bag.items():
        total += count + (count * get_bag_count(bags[sub_bag]))
    return total


bag_count = 0
bag_count = get_bag_count(bags["shiny gold"])
print(bag_count)
