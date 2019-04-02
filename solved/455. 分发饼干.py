"""
第一种是自己写的，从两个数组后面向前遍历，不够贪心（应该还是有一点贪心的吧），所以不是很快。
第二种是贪心算法，因为每个小朋友只能获得一个饼干，所以从前向后遍历饼干数组，然后看取出的饼干是否能给当前的小朋友，
如果能那么接着去取饼干给下一个朋友，如果不能则继续向后取饼干。如果，某个时刻所有的孩子都给了饼干，那么就不用在遍历
了，直接返回所有的小朋友，但是如果饼干全部分发完，也就返回当前的ret。
其实，仔细一想两种方法是一样的，不过躯体的实施不同。所以两个都是贪心的。
"""
class Solution:
    def findContentChildren(self, g, s):
        # 平平无奇，没用贪心
        # g.sort()
        # s.sort()
        # indexChild = len(g)-1
        # indexCookie = len(s)-1
        # ret = 0
        # while indexChild >= 0 and indexCookie >= 0:
        #     if g[indexChild] <= s[indexCookie]:
        #         ret += 1
        #         indexCookie -= 1
        #     indexChild -= 1
        # return ret

        # 贪心
        g.sort()
        s.sort()
        ret = 0
        numChildren = len(g)
        indexChild = 0
        for cookie in s:
            if cookie >= g[indexChild]:
                ret += 1
                indexChild += 1
                if indexChild == numChildren:
                    return ret
        return ret


solve = Solution()
g = [1,2, 3]
s = [1,1]
print(solve.findContentChildren(g, s))