""" This program takes a grid of # and - where each hash reps a mine and each dash a mine-free spot
 and returns a grid where each dash is replace by a digit indicating the nos of mines immediately adjacent to the
spot
"""


def mine_count(grid):
    m, n = len(grid), len(grid[0])
    result = [[0 for j in range(n)] for i in range(m)]
    # using list comprehension for the output grid
    # code below iterates through the 2D list comparing '#' and returning '#'
    # whilst adding the count to the x,y variables if not '#'
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                result[i][j] = "#"
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if result[x][y] != "#":
                            result[x][y] += 1
    for i in range(m):
        for j in range(n):
            if result[i][j] != "#":
                result[i][j] = str(result[i][j])
    return result


grid = [["-", "-", "#", "-"],
        ["-", "#", "-", "-"],
        ["-", "-", "-", "#"],
        ]

# Calling the function to print out the output

print(mine_count(grid))
