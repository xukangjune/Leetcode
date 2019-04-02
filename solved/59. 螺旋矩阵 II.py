class Solution:
    def __init__(self):
        self.count = 1
        self.array = None
        self.i = 0
        self.j = 0
        self.turn = 1
        self.n = 0

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        k = (n - 1) / 2
        self.array = [[0 for i in range(n)] for i in range(n)]
        print(self.array)
        while self.count <= n * n:
            if self.turn == 1:  # ���������
                if self.i < k:
                    while self.isLegal():  # ����
                        self.array[self.i][self.j] = self.count
                        self.count += 1
                        self.j += 1
                    self.j -= 1
                    self.i += 1
                else:
                    while self.isLegal():  # ����
                        self.array[self.i][self.j] = self.count
                        self.count += 1
                        self.j -= 1
                    self.j += 1
                    self.i -= 1
                self.turn *= -1  # �ı�״ֵ̬
                continue
            else:
                if self.j < k:  # ����
                    while self.isLegal():
                        self.array[self.i][self.j] = self.count
                        self.count += 1
                        self.i -= 1
                    self.i += 1
                    self.j += 1
                else:
                    while self.isLegal():  # ����
                        self.array[self.i][self.j] = self.count
                        self.count += 1
                        self.i += 1
                    self.i -= 1
                    self.j -= 1
                self.turn *= -1
                continue

    def isLegal(self):
        if 0 <= self.i < self.n and 0 <= self.j < self.n and self.array[self.i][self.j] == 0:
            return True
        return False


solve = Solution()
solve.generateMatrix(6)
print(solve.array)