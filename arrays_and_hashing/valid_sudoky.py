# example board:
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]


def is_valid_sudoku(board):
    hor = [set() for _ in range(9)]
    ver = [set() for _ in range(9)]
    sqr = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):

            val = board[i][j]
            if val == ".":
                continue
            if val in hor[i]:
                return False
            if val in ver[j]:
                return False
            if val in sqr[3 * (i // 3) + (j // 3)]:
                return False
            hor[i].add(val)
            ver[j].add(val)
            sqr[3 * (i // 3) + (j // 3)].add(val)
    return True
