"""
这一题我用了不同的方法，首先想到的是逐层剥离的方法，每一以1为一个单位，每次都剥离高度1，最后累加，但是这个到最后
一个用例时就失败了，后来用改进版的剥离，最后也还是超时了，时间复杂度O（n*n）。
后来还是规规矩矩用来双指针的方法，右指针先向右找比左指针大的一项，如果大，说明就可以收集雨水。但是这样会有一个问题，
那就是在结尾处，如果一直减小，虽然可以收集雨水但是没有累加上去，因此我们可以方向再遍历一回数组，但实际上可以不用这
么做，只要反向遍历到最后的左指针出就好了。
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 太慢
        # ret = 0
        # left = 0
        # n = len(height)
        # right = n -1
        # while left < right:
        #     while left <= right and not height[left]:
        #         left += 1
        #     while right >= left and not height[right]:
        #         right -= 1
        #     for i in range(left, right+1):
        #         if height[i]:
        #             height[i] -= 1
        #         else:
        #             ret += 1
        # return ret

        # 这是通过的一种解答，还可以
        # ret = 0
        # left = 0
        # right = left + 1
        # n = len(height)
        # temp = 0
        # while right < n:
        #     threshold = height[left]
        #     if height[right] < threshold:
        #         temp += height[right]
        #         right += 1
        #     else:
        #         ret += threshold * (right - left - 1) - temp
        #         left = right
        #         right = left + 1
        #         temp = 0
        # n = left
        # right -= 1
        # temp = 0
        # left = right - 1
        # while left >= n:
        #     threshold = height[right]
        #     if height[left] < threshold:
        #         temp += height[left]
        #         left -= 1
        #     else:
        #         ret += threshold * (right - left - 1) - temp
        #         right = left
        #         left = right - 1
        #         temp = 0
        # return ret

        # 尝试另一种，也是逐层剥离
        # 不行，还是超时间限制了
        if not height:
            return 0
        ret = 0
        left = 0
        n = len(height)
        right = n -1
        temp = sorted([num for num in height if num > 0])
        k = 0
        m = len(temp)
        num = 0
        if not temp:
            return 0
        while left < right and k < m:
            minuend = temp[k] - num
            while left <= right and not height[left]:
                left += 1
            while right >= left and not height[right]:
                right -= 1
            for i in range(left, right+1):
                if height[i]:
                    height[i] -= minuend
                else:
                    ret += minuend
            num = temp[k]
            k += 1
        return ret





solve = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [0,0,0,0,1,0,1]
# height = [2,0,2]
height = []
print(solve.trap(height))