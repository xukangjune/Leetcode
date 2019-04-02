"""
这一题我之前一直纠结的是如果左右两个指针的数相等怎么办，但是实际上不影响，可以随便选择一边向中间靠近。因为有下面三种情况：
假设左右两边的指针分别为left,right，这两个位置里面的两个坐标为leftmid,rightmid。
1，如果leftmid和rightmid比left和right都要大，那么无论是先将left设为leftmid还是right设为rightmid，最终结果都是一样的，即
left=>leftmid， right=>rightmid。
2，如果leftmid和rightmid比left和right都要小，那么无论动哪一个，开始的值肯定比现在的ret小（因为不仅距离短，而且高度小），这种
所以可以一直移动，而不用考虑后果。情况一直延续到left和right最终的值都大于现在的left和right
3，如果leftmid和rightmid比left和right一个小一个大，同2，无论移动哪一个（left or right）都会比现在的ret小（1，高度相同，
距离减小；2，高度小，距离减小），所以最后的结果就是left和right都找到比现在更大的值。
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ret = min(height[left], height[right]) * (right - left)
        print(ret)
        # 原本的，在height[left]==height[right]时采取了一条很笨的方法
        # while left < right:
        #     temp = min(height[left], height[right]) * (right - left)
        #     ret = temp if temp > ret else ret
        #     if height[left] < height[right]:
        #         left += 1
        #     elif height[left] > height[right]:
        #         right -= 1
        #     else:
        #         if height[left + 1] > height[right - 1]:
        #             left += 1
        #         else:
        #             right -= 1
        # return ret

        # 稍微改进
        while left < right:
            l = right - left
            if height[left] > height[right]:
                temp = l * height[right]
                right -= 1
            else:
                temp = l * height[left]
                left += 1
            ret = temp if temp > ret else ret
            print(ret)
        return ret



solve = Solution()
# height = [1,8,6,2,5,4,8,3,7]
# height = [1,2,1]
height = [1,2,4,3]
print(solve.maxArea(height))