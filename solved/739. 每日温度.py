"""
本来想优化，用了字典来存同一温度的日期，然后栈只存温度，通过温度来去找日期，这么做比较慢。
后来，就用最传统的栈来做，栈存储日期（也就是下标）。
"""
class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        ret = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret

        # 这样写还慢一点
        # n = len(T)
        # ret = [0] * n
        # stack = [T[0]]
        # tempToDays = {T[0]:[0]}
        # i = 1
        # while i < n:
        #     while stack and T[i] > stack[-1]:
        #         t = stack.pop()
        #         for index in tempToDays[t]:
        #             ret[index] = i - index
        #         del tempToDays[t]
        #     if T[i] not in tempToDays:
        #         tempToDays[T[i]] = []
        #     tempToDays[T[i]].append(i)
        #     if not stack or T[i] < stack[-1]:
        #         stack.append(T[i])
        #     i += 1
        # return ret


solve = Solution()
# T = [73, 74, 75, 71, 69, 72, 76, 73,90]
# T = [1]
T = [89,62,70,58,47,47,46,76,100,70]
print(solve.dailyTemperatures(T))

