import copy
import puzzleinput
rows = [[True if c == "#" else False for c in li] for li in puzzleinput.lines]
cubes = [rows]


def count_active_cubes_around(x, y, z, cubes):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if 0 == i == j == k:
                    continue
                new_z = z + i
                new_y = y + j
                new_x = x + k
                if new_z == -1 or new_y == -1 or new_x == -1:
                    continue
                try:
                    if cubes[new_z][new_y][new_x]:
                        count += 1
                except IndexError:
                    pass
    return count


def expand_cubes(cubes):
    new_cubes = []
    for z in range(len(cubes) + 2):
        new_column = []
        for y in range(len(cubes[0]) + 2):
            new_row = []
            for x in range(len(cubes[0][0]) + 2):
                try:
                    if not x or not y or not z:
                        raise IndexError
                    state = cubes[z - 1][y - 1][x - 1]
                except IndexError:
                    state = False
                new_row.append(state)
            new_column.append(new_row)
        new_cubes.append(new_column)
    return new_cubes


for _ in range(6):
    cubes = expand_cubes(cubes)
    next_cubes = copy.deepcopy(cubes)
    for z, column in enumerate(cubes):
        for y, row in enumerate(column):
            for x, state in enumerate(row):
                active_neighbors = count_active_cubes_around(x, y, z, cubes)
                if state:
                    if active_neighbors not in {2, 3}:
                        next_cubes[z][y][x] = not state
                    continue
                if active_neighbors == 3:
                    next_cubes[z][y][x] = not state
    cubes = next_cubes

total = 0
for column in cubes:
    for row in column:
        total += sum(row)

print(total)
