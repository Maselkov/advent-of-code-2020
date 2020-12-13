import puzzleinput
import math

buses = puzzleinput.lines[1].split(",")
offsets = []
offset = 0
for bus in buses:
    if bus.isdigit():
        offsets.append(offset)
    offset += 1

buses = [int(bus) for bus in buses if bus.isdigit()]
product = math.prod(b for b in buses if b)
step = buses[0]
bus_count = 2
start = step
while bus_count < len(buses) + 1:
    for i in range(start, product, step):
        for bus, offset in zip(buses[:bus_count], offsets[:bus_count]):
            if (i + offset) % bus:
                break
        else:
            start = i
            step = math.prod(buses[:bus_count])
            bus_count += 1
            break
print(i)
