"""
本地是在一个二维字符数组中寻找给定的单词，其实和走迷宫是一样的。先从二维数组中找到与第一个字母相同的位置，从此位置开始递归。因为每个字母只能
用一次（类比于迷宫中走回已经走过的地方），所以设置一个等大flag数组。每走过一个地方设置新的值。回溯是改成原来的值。在递归的过程中，如果发现
递归的次数等于单词的长度（说明已经全部匹配），这是一路返回True。如果一个位置的四个方向遍历完毕，没有合适的路径，这时候就要回溯。继续上层
函数，可能上层函数继续遍历也有可能也返回到跟更上一层。
"""


class Solution(object):
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.length = 0
        self.word = None
        self.board = None
        self.flag = None

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        self.length = len(word)
        self.word = word
        self.board = board
        self.flag = [[0] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == self.word[0]:
                    print(i, j)
                    if self.func(i, j, curLen=0):
                        return True
                    continue
        return False

    def func(self, curI, curJ, curLen):
        self.flag[curI][curJ] = 1
        curLen += 1
        if curLen == self.length:
            return True
        else:
            for direction in self.directions:
                if self.legal(curI+direction[0], curJ+direction[1]) and \
                self.board[curI+direction[0]][curJ+direction[1]] == self.word[curLen]:
                    if self.func(curI+direction[0], curJ+direction[1], curLen):
                        return True
                    else:
                        continue
            self.flag[curI][curJ] = 0
            return

    def legal(self, i, j):
        return 0 <= i < self.m and 0 <= j < self.n and self.flag[i][j] == 0


solve = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(solve.exist(board, word))