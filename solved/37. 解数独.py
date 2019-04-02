"""
和八皇后问题类似，这里用三个容器来记录已有的状态，第一个是每行的，一个是每列的，一个是每块的。还用一个数组列表记录没有填写
的位置。最后在深搜的时候就用这个数组一直递归下去。每递归一次，如果合适，那么三个容器状态都要更新。当最后，如果递归的深度使得
k==n，说明已经找到一个合适的了，返回就OK了。
"""
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        raws = list(map(list, zip(*board)))
        blocks = [set() for i in range(9)]
        unfilled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    blocks[i//3*3+j//3].add(board[i][j])
                else:
                    unfilled.append([i, j])
        n = len(unfilled)


        def isLegal(i, j, char):
            return char not in board[i] and char not in raws[j] and char not in blocks[i//3*3+j//3]

        def DFS(k):
            if k == n:
                return True

            i = unfilled[k][0]
            j = unfilled[k][1]
            for num in ["5","3","1","2","7","4","6","8","9"]:
                if isLegal(i, j, num):
                    board[i][j] = num
                    raws[j][i] = num
                    blocks[i//3*3+j//3].add(num)
                    if not DFS(k+1):
                        board[i][j] = "."
                        raws[j][i] = "."
                        blocks[i // 3 * 3 + j // 3].remove(num)
                    else:
                        return True
            return False

        DFS(0)


solve = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solve.solveSudoku(board)
print(board)