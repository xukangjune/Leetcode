"""
第一种方法是我自己写的，先将字符串换成数组（因为字符串不好更改），然后先执行一次循环操作，将所有的小于2*k的前k个字符串转化。然后判断剩下的字符
是多上，根据不同的条件操作。
在别人的解答中看到有人用递归解答，也可以但是觉得有点小题大做。有一种更简单的解法，先将字符串转为数组，然后在数组上每隔2*k个位置进行一次k个字符
的操作。很简单，而且涵盖了所有的情况。
"""
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 我写的，注意边界条件
        # s = list(s)
        # n = len(s)
        # i = 0
        # while i + 2*k <= n:
        #     count = 0
        #     while count < k // 2:
        #         s[i+count], s[i+k-1-count] = s[i+k-1-count], s[i+count]
        #         count += 1
        #     i += 2 * k
        #     print(i)
        # if i < n < i+k:
        #     count = 0
        #     while count < (n-i) // 2:
        #         s[i+count], s[n-1-count] = s[n-1-count], s[i+count]
        #         count += 1
        # elif i+k <= n:
        #     count = 0
        #     while count < k // 2:
        #         print(i+count, i+k-1-count)
        #         s[i + count], s[i + k - 1 - count] = s[i + k - 1 - count], s[i + count]
        #         count += 1
        #     i += k
        # return ''.join(s)

        # 看别人写的，用的递归
        # 还是不用递归，用这种方法觉得更好
        n = len(s)
        s = list(s)
        for i in range(0, n, 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s)


solve = Solution()
s = "abcdefghijkl"
# s = "abcd"
k = 3
print(solve.reverseStr(s, k))