"""
这一题使用的倒推法，先将数组排序，然后从最大的数开始，每次假如一个小数时，先将原本的数组的最后一位放到第一位。我开始用了一个辅助数组，每次将
处理好的数放到辅助数组中，但是这样开辟了一个新的空间，空间复杂度较大。
后来看到别人的解法，原来可以直接在原为操作，先将数组排序，然后从尾到头开始逐个的处理，处理的方式和前面的解法一样。本问题实际上可以看成是一个
动态规划的问题，对数组进行从后向前的遍历时，就是在处理一个个子问题。
我的另一个想法是能不能通过下标来直接赋值，即先准备一个等大的数组，然后对排序好的原数组进行遍历操作，原数组每个下标都对应着新数组的下标。我觉得
这样行得通，因为数组的变换是有一定的规律的，但是现在数学水平不够，不知道这个对应关系是什么。
"""
class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        # 这是我开始写的，引入了新的数组，空间复杂度为O（n）
        # ret = [deck[-1]]
        # for num in deck[-2::-1]:
        #     ret.insert(0, ret.pop())
        #     ret.insert(0, num)
        # return ret

        # 参考网上的一种写法，原理是一样的，只是没有用到额外的空间
        n = len(deck)
        if n > 2:
            for i in range(n-3, -1, -1):
                deck.insert(i+1, deck.pop())
        return deck


solve = Solution()
deck = [17,13,2,3,5,7]
print(solve.deckRevealedIncreasing(deck))