"""
我真的好笨呀！（气不过）这么简单的题目，主要一开始就想歪了，思路不对。
应该是这样的，假设所给的数字为n。先找出根节点，根节点的左子树和右子树节点的和一定位n-1。那么所以左子树的个数可以为0个，也可以为n-1个。而
右子树的个数与左子树共轭。再假设左子树的个数为i个，则右子树为n-1-i个。左子树的i个节点又可以看成是一个子问题（动态规划），同样右子树也是。
所以此种情况下的种类为dp[i] * dp[n-1-i]（i可以从0遍历到n-1）。这样最后将总的结果求和。
本题，我先设置了一个类属性，这样所有的实例都可以使用。该类属性是一个字典，里面存的是n个数字时其二叉树的种类（这点很重要！！！），而不是数字为
n时，所有的种类数。
"""
class Solution:
    dp = {}
    dp[0] = 1
    dp[1] = 1
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp:
            return self.dp[n]
        ret = 0
        for i in range(n):
            ret += self.numTrees(i) * self.numTrees(n-1-i)
        self.dp[n] = ret
        return ret


solve = Solution()
print(solve.numTrees(3))