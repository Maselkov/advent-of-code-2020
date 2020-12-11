import puzzleinput
import itertools
chairs = [list(row) for row in puzzleinput.lines]
EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"
DIRECTIONS = [p for p in itertools.product(range(-1, 2), repeat=2)]
DIRECTIONS.remove((0, 0))


def count_visible_occupied_chairs(x1, y1):
    seat_count = 0

    def check_in_direction(x_direction, y_direction):
        x2 = x1 + x_direction
        y2 = y1 + y_direction
        while x2 > -1 and y2 > -1 and y2 < len(chairs) and x2 < len(chairs[0]):
            if chairs[y2][x2] == EMPTY:
                break
            if chairs[y2][x2] == OCCUPIED:
                return 1
            x2 += x_direction
            y2 += y_direction
        return 0

    for dir in DIRECTIONS:
        seat_count += check_in_direction(*dir)
    return seat_count


state_changed = True
while state_changed:
    state_changed = False
    new_grid = []
    for y, row in enumerate(chairs):
        new_row = []
        for x, type in enumerate(row):
            if type != FLOOR:
                adjacent = count_visible_occupied_chairs(x, y)
                if type == EMPTY and not adjacent:
                    type = OCCUPIED
                    state_changed = True
                elif type == OCCUPIED and adjacent >= 5:
                    type = EMPTY
                    state_changed = True
            new_row.append(type)
        new_grid.append(new_row)
    chairs = new_grid[:]
occupied_total = 0
for row in chairs:
    occupied_total += row.count(OCCUPIED)
print(occupied_total)
