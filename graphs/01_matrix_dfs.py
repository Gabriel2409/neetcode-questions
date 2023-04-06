# count nb of paths from top left to bottom right.
# can only move on 0
# matrix = [[0,0,0], [1,0,0], [1,1,0]] => total = 2


def matrix_dfs(mat, i=0, j=0, visited=None)-> int:
    nb_rows = len(mat)
    nb_cols = len(mat[0])

    # speed up
    cache = {}
    if (i,j) in cache:
        return cache[(i,j)]

    if not visited:
        visited = set()

    if i < 0 or j < 0 or i >= nb_rows or j >= nb_cols or (i, j) in visited or mat[i][j] == 1:
        return 0
    if i == nb_rows - 1 and j == nb_cols - 1:
        return 1

    visited.add((i, j))

    count = 0
    count += matrix_dfs(mat, i + 1, j, visited)
    count += matrix_dfs(mat, i - 1, j, visited)
    count += matrix_dfs(mat, i, j + 1, visited)
    count += matrix_dfs(mat, i, j - 1, visited)
    visited.remove((i,j))
    cache[(i,j)] = count
    return count

mat = [[0,0,0], [1,0,0], [1,1,0]] 
# mat = [[0,0], [1,0]] 
print(matrix_dfs(mat))
