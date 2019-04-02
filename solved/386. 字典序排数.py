"""
第一个是我写的，shit，用了内置的方法和排序。因为字符串排序用的就是字典序，所以这种方法得要先将整数先转为字符串，然后排序。
算法的时间复杂度和空间复杂度都要大于O(n)。
下面的是参考别人的方法，非常巧妙。
首先生成一个大小为n的返回数组。然后遍历数组，对数组的每个位置赋值，最后数组正好将n个数填满。问题是怎么确定每个位置上填的数。
首先第一点可以确定，第一个位置上填1。然后以此为起点。下一个位置的数由当前位置的数决定。从共有三个节点：1，直接乘上10；2，直接
加1；3，循环检查num的最后一位是否为9或等于n，如果这样对10整除。并对循环后的数加1。这三个条件依次检查。
"""
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 投机取巧，用字符串, 感觉不是题目要考的点
        # return [int(i) for i in sorted([str(i) for i in range(1, n+1, 1)])]

        # 这种方法比较好
        ret = [0] * n
        num = 1
        for i in range(n):
            ret[i] = num
            # 计算下一个位置的num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num == n:
                    num = num // 10
                num += 1
        return ret

solve = Solution()
print(solve.lexicalOrder(200))