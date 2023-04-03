def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    def is_word_in_board(board, word):
        def dfs(i, j, pos):
            if (i,j,pos) in cached:
                return cached[(i,j,pos)]
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[pos]:
                return False
            if (i, j) in visit:
                return False
            if pos == len(word) - 1:
                return True

            visit.add((i, j))
            found = (
                dfs(i, j + 1, pos + 1)
                or dfs(i, j-1, pos + 1)
                or dfs(i - 1, j, pos + 1)
                or dfs(i + 1, j, pos + 1)
            )
            visit.remove((i, j))
            if found:
                cached[(i,j,pos)] = found
            return found

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    visit = set()
                    cached = {}
                    found = dfs(i, j, 0)
                    if found:
                        return True
        return False

    final = []
    for word in words:
        if is_word_in_board(board, word):
            final.append(word)
    return final

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

board = [["a","a"]]
words = ["aa"]

board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["eaafgdcba","eaabcdgfa"]


board = [["a","b","e"],["b","c","d"]]
words = ["abcdeb"]
print(find_words(board, words))