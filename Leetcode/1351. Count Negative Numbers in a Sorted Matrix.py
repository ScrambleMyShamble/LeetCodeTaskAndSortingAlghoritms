grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
unpacked = sum(grid, [])

print(len([el for el in unpacked if el < 0]))
