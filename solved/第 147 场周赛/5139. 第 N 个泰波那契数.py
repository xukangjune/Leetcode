class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1
        first = 0
        second = third = 1
        for i in range(3, n+1):
            temp = first + second + third
            first = second
            second = third
            third = temp
        return third


solve = Solution()
print(solve.tribonacci(25))