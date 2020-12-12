import puzzleinput
import math


def rotate(x2, y2, degrees):
    angle = math.radians(degrees)
    cos = math.cos(angle)
    sin = math.sin(angle)
    x3 = cos * x2 - sin * y2
    y3 = sin * x2 + cos * y2
    return round(x3), round(y3)


x = 10
y = -1
traveled_x = 0
traveled_y = 0
for line in puzzleinput.lines:
    action = line[0]
    value = int(line[1:])
    if action == "F":
        traveled_x += value * x
        traveled_y += value * y
    if action == "N":
        y -= value
    if action == "S":
        y += value
    if action == "E":
        x += value
    if action == "W":
        x -= value
    if action == "R":
        x, y = rotate(x, y, value)
    if action == "L":
        x, y = rotate(x, y, -value)
print(abs(traveled_x) + abs(traveled_y))
