import puzzleinput

earliest = int(puzzleinput.lines[0])
buses = puzzleinput.lines[1].split(",")

best_bus = None
best_time = float("inf")
for bus in buses:
    if bus.isdigit():
        bus = int(bus)
        time_to_wait = (((earliest // bus) + 1) * bus) % earliest
        if time_to_wait < best_time:
            best_bus = bus
            best_time = time_to_wait

print(best_bus * best_time)
