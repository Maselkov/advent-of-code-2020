import puzzleinput

x = 0
y = 0
x_direction = 1
y_direction = 0
for line in puzzleinput.lines:
    action = line[0]
    value = int(line[1:])
    if action == "F":
        x += x_direction * value
        y += y_direction * value
    if action == "N":
        y -= value
    if action == "S":
        y += value
    if action == "E":
        x += value
    if action == "W":
        x -= value
    if action == "R":
        for i in range(value // 90):
            if x_direction == 1:
                x_direction = 0
                y_direction = 1
            elif y_direction == 1:
                x_direction = -1
                y_direction = 0
            elif x_direction == -1:
                y_direction = -1
                x_direction = 0
            else:
                x_direction = 1
                y_direction = 0
    if action == "L":
        for i in range(value // 90):
            if x_direction == 1:
                x_direction = 0
                y_direction = -1
            elif y_direction == -1:
                x_direction = -1
                y_direction = 0
            elif x_direction == -1:
                y_direction = 1
                x_direction = 0
            else:
                x_direction = 1
                y_direction = 0

print(abs(x) + abs(y))
