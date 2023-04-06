# find length of shortest path
# can only move on 0
# matrix =
# [
# [0,0,0,0],
# [1,0,0,1],
# [1,0,0,0]
# ]
# => total = 6
from collections import deque


def matrix_bfs(mat) -> int:
    nb_rows = len(mat)
    nb_cols = len(mat[0])
    visited = set()
    q = deque()

    q.append((0, 0))
    visited.add((0, 0))

    length = 0

    while q:
        # for loop ensures we pop all the coordinates where path is of same length
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == nb_rows - 1 and j == nb_cols - 1:
                return length

            adjascents = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]

            for r, c in adjascents:
                if (
                    r < 0
                    or c < 0
                    or r >= nb_rows
                    or c >= nb_cols
                    or ((r, c)) in visited
                    or mat[r][c] == 1
                ):
                    continue

                q.append((r, c))
                visited.add((r, c))
        length = length + 1


print(matrix_bfs([[0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0]]))
