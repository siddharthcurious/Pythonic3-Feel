def numberOfWalls(board1):
    if not board1:
        return 0

    board = []
    for row in board1:
        board.append(list(row))

    row = len(board)
    col = len(board[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                dfs(board, row, col, i, j)
                count += 1
    return count

def dfs(board, row, col, x, y):
    if board[x][y] == 'O':
        return

    board[x][y] = 'O'
    if x != 0:
        dfs(board, row, col, x - 1, y)
    if x != row - 1:
        dfs(board, row, col, x + 1, y)
    if y != 0:
        dfs(board, row, col, x, y - 1)
    if y != col - 1:
        dfs(board, row, col, x, y + 1)

board = ["XOXOXX", "XOOXOO"]
r = numberOfWalls(board)
print(r)
