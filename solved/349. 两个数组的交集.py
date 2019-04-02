"""
这题分别遍历两个排序后数组，看之间的相对大小。如果相等，还有看看是否已经在ret数组中存在了，不然会导致重复元素。我在ret数组中先加了一个初始
值，这样就不用在比较时没回都要判断数组是否为空。
"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ret = ['ZERO']
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] != ret[-1]:
                    ret.append(nums1[i])
                i += 1
                j += 1
        del ret[0]
        return ret


solve = Solution()
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
nums1 = [1,2,2,1]
nums2 = [2,2]
print(solve.intersection(nums1, nums2))