class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = []
        for i in range(len(board)):
            L1 = []
            for j in range(len(board[0])):
                L1.append(0)
            visited.append(L1)

        for row in board:
            for ch in row:
                if ch == word[0]:
                    pass

        def dfs_search(ch):
            pass





if __name__ == "__main__":

    s = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    word = "ABCCED"
    r = s.exist(board, word)
    print(r)


