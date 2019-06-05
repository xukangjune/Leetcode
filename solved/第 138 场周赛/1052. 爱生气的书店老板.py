class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        n = len(grumpy)
        if X >= n:
            return sum(customers)


        ret = 0
        for i, num in enumerate(grumpy):
            if num == 0:
                ret += customers[i]

        for i in range(X):
            ret += customers[i] if grumpy[i] else 0

        temp = ret
        for i in range(1, n-X+1):
            if not grumpy[i+X-1]:
                temp -= customers[i-1] if grumpy[i-1] else 0
            elif grumpy[i-1]:
                temp += customers[i+X-1] - customers[i-1]
                ret = max(temp, ret)
            else:
                temp += customers[i+X-1]
                ret = max(ret, temp)

        return ret


solve = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(solve.maxSatisfied(customers, grumpy, X))