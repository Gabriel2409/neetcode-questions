# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

from collections import deque


def shortest_path_bin_matrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    nb_rows = len(grid)
    nb_cols = len(grid[0])

    visited = set()
    q = deque()
    q.append((0, 0))
    visited.add((0, 0))

    length = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == nb_rows - 1 and j == nb_cols - 1:
                return length
            neigh = [
                (i, j + 1),
                (i, j - 1),
                (i + 1, j),
                (i + 1, j - 1),
                (i + 1, j + 1),
                (i - 1, j),
                (i - 1, j - 1),
                (i - 1, j + 1),
            ]

            for r, c in neigh:
                if (
                    r < 0
                    or c < 0
                    or r >= nb_rows
                    or c >= nb_cols
                    or (r, c) in visited
                    or grid[r][c] == 1
                ):
                    continue
                q.append((r, c))
                visited.add((r, c))

        length += 1

    return -1

mat = [[0,0,0],[1,1,0],[1,1,0]]
mat = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
print(shortest_path_bin_matrix(mat))