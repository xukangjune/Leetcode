"""
原来写的真垃圾，其实整个数组可以看成是一个一维的，只不过要展开。
第二种方法直接用的数组排数的规律性，是最快的。
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    # 什么垃圾， 又长又臭
    #     if not matrix or not matrix[0]:
    #         return False
    #     list1 = [a[0] for a in matrix]
    #     index1 = self.binarySearch(list1, target)
    #     if target < matrix[index1][0]:
    #         index1 -= 1
    #     index2 = self.binarySearch(matrix[index1], target)
    #     return True and matrix[index1][index2] == target or False
    #
    # def binarySearch(self, theList, target):
    #     first = 0
    #     last = len(theList) - 1
    #     while first < last:
    #         middle = (first + last) // 2
    #         if theList[middle] == target:
    #             return middle
    #         elif theList[middle] > target:
    #             last -= 1
    #         else:
    #             first += 1
    #     return first

    # 二分法
    #     if matrix:
    #         m = len(matrix)
    #         n = len(matrix[0])
    #         print(m, n)
    #         left = 0
    #         right = m * n - 1
    #         while left <= right:
    #             print(left, right)
    #             mid = (left + right) // 2
    #             print(mid // n)
    #             if matrix[mid // n][mid % n] < target:
    #                 left = mid + 1
    #             elif matrix[mid//n][mid%n] > target:
    #                 right = mid - 1
    #             else:
    #                 return True
    #     return False

    # 根据数组的特点
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            col = 0
            row = n-1
            while col < m and row >= 0:
                if matrix[col][row] == target:
                    return True
                elif matrix[col][row] > target:
                    row -= 1
                else:
                    col += 1
        return False



solve = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(solve.searchMatrix(matrix, target))