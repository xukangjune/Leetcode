"""
没啥解题技巧
"""
class Solution:
    def gameOfLife(self, board) -> None:
        m = len(board)
        n = len(board[0])
        change = set()
        for i in range(m):
            for j in range(n):
                count = 0
                for p in range(i-1, i+2):
                    for q in range(j-1, j+2):
                        if 0 <= p < m and 0 <= q < n and board[p][q]:
                            count += 1
                if board[i][j]:
                    if not 2 <= count - 1 <= 3:
                        change.add((i, j))
                elif not board[i][j] and count == 3:
                    change.add((i, j))
        for pos in change:
            board[pos[0]][pos[1]]  = board[pos[0]][pos[1]] *(-1) + 1


solve = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
solve.gameOfLife(board)
print(board)