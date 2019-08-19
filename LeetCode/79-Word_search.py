import numpy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        wlen = len(word)
        rows = len(board)
        cols = len(board[0])

        if word == "":
            return True

        visited = [ [ 0 for _ in range(cols)] for _ in range(rows)]

        def isSafe(i, j):
            if i >= 0 and i < rows and j >= 0 and j < cols and visited[i][j] == 0:
                return True
            return False

        def dfs(board, word, cons, r, c, wlen):
            if isSafe(r+1, c):
                if board[r+1][c] == word[cons] and cons == wlen-1:
                    return True
                elif board[r+1][c] == word[cons]:
                    visited[r+1][c] = 1
                    return dfs(board, word, cons+1, r+1, c, wlen)

            if isSafe(r-1, c):
                if board[r-1][c] == word[cons] and cons == wlen-1:
                    return True
                elif board[r-1][c] == word[cons]:
                    visited[r-1][c] = 1
                    return dfs(board, word, cons+1, r-1, c, wlen)

            if isSafe(r, c+1):
                if board[r][c+1] == word[cons] and cons == wlen-1:
                    return True
                elif board[r][c+1] == word[cons]:
                    visited[r][c+1] = 1
                    return dfs(board, word, cons+1, r, c+1, wlen)

            if isSafe(r, c-1):
                if board[r][c-1] == word[cons] and cons == wlen-1:
                    return True
                elif board[r][c-1] == word[cons]:
                    visited[r][c-1] = 1
                    return dfs(board, word, cons+1, r, c-1, wlen)
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    return dfs(board, word, 0, i, j, wlen)
        return False

if __name__ == "__main__":

    s = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    word = "ASFCB"

    board = [
        ["C", "A", "A"],
        ["A", "A", "A"],
        ["B", "C", "D"]
    ]
    "AAB"
    r = s.exist(board, word)
    print(r)


