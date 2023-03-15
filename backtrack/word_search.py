# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent
# cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


def exist(board: list[list[str]], word: str) -> bool:
    def find_next(i, j, ind, forbidden):
        nonlocal found
        if ind == len(word):
            found = True
            return
        if i < 0 or i >= len(board):
            return
        if j < 0 or j >= len(board[0]):
            return

        if (i, j) in forbidden:
            return

        if board[i][j] == word[ind]:
            forbidden = forbidden.copy()
            forbidden.add((i, j))
            find_next(i + 1, j, ind + 1, forbidden)
            find_next(i - 1, j, ind + 1, forbidden)
            find_next(i, j + 1, ind + 1, forbidden)
            find_next(i, j - 1, ind + 1, forbidden)

    found = False
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == word[0]:
                find_next(i, j, 0, set())

    return found


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))
