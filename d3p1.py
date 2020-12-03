import puzzleinput

right = 3
down = 1

grid = puzzleinput.lines
x = 0
y = 0
trees_encountered = 0
while y < len(grid):
    if grid[y][x % len(grid[y])] == "#":
        trees_encountered += 1
    y += down
    x += right
print(trees_encountered)
