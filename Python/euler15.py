import sys

arg = int(sys.argv[1])

grid = []
for i in range(arg+1):
    grid.append([])

for i in range(arg+1):
    grid[i].append(1)

for i in range(arg):
    grid[0].append(1)

for i in range(1, arg+1):
    for j in range(1, arg+1):
        grid[i].append(grid[i-1][j] + grid[i][j-1])


print(grid)
