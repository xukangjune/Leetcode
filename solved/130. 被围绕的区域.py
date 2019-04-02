"""
这一题大家用的方法也差不多，先从边界处的O使用深度优先搜索，找出所有相连的O，并进行递归，先将这些不会改变的O重新标记为@。
最后遍历一遍board，将其中所有的@改为O，其余的全部改为X。
"""
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
            col = len(board[0])
            row = len(board)
            print(board)

            def dfs(i, j):
                board[i][j] = "@"
                for direction in directions:
                    nextI = i + direction[0]
                    nextJ = j + direction[1]
                    if 0 < nextI < row and 0 < nextJ < col and board[nextI][nextJ] == "O":
                        dfs(nextI, nextJ)

            for i in (0, row - 1):
                for j in range(col):
                    dfs(i, j) if board[i][j] == 'O' else None
            for j in (0, col - 1):
                for i in range(row):
                    dfs(i, j) if board[i][j] == 'O' else None
            print(board)
            for i in range(row):
                for j in range(col):
                    board[i][j] = 'O' if board[i][j] == '@' else 'X'
            print(board)

solved = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solved.solve(board)