import puzzleinput

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

grid = puzzleinput.lines
product = 1
for right, down in slopes:
    x = 0
    y = 0
    trees_encountered = 0
    while y < len(grid):
        if grid[y][x % len(grid[y])] == "#":
            trees_encountered += 1
        x += right
        y += down
    product *= trees_encountered
print(product)
