import puzzleinput
import copy
chairs = [list(row) for row in puzzleinput.lines]
EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"


def count_adjacent_occupied_chairs(x, y):
    seats = 0
    for i in range(-1, 2):
        if y + i < 0:
            continue
        for j in range(-1, 2):
            if x + j < 0:
                continue
            if not i and not j:
                continue
            try:
                if chairs[y + i][x + j] == OCCUPIED:
                    seats += 1
            except IndexError:
                continue
    return seats


state_changed = True
while state_changed:
    state_changed = False
    new_grid = []
    for y, row in enumerate(chairs):
        new_row = []
        for x, type in enumerate(row):
            adjacent = count_adjacent_occupied_chairs(x, y)
            if type == EMPTY and not adjacent:
                type = OCCUPIED
                state_changed = True
            elif type == OCCUPIED and adjacent >= 4:
                type = EMPTY
                state_changed = True
            new_row.append(type)
        new_grid.append(new_row)
    chairs = new_grid[:]
occupied_total = 0
for row in chairs:
    occupied_total += row.count(OCCUPIED)
print(occupied_total)
