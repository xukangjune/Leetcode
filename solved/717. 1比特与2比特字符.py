"""
这一题关键要将最后一位提出来，然后对前面的数组遍历。首先，如果元素等于1，那么向后移两位，如果等于零，只要移动一位。等到遍历后，如果最后的i值
等于数组的长度，表示不满足，反之，就满足。
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits) - 1
        i = 0
        while i < length:
            i += 1 if bits[i] == 0 else 2
        return i == length


solve = Solution()
bits = [1, 1, 1, 1, 0]
print(solve.isOneBitCharacter(bits))