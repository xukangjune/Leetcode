"""
这一题如果用内置的filter函数过滤出一个奇数数组和一个偶数数组，然后对着数组进行重新组合也可以达到要求，这是比较容易想到的方法，但是该方法的空
间要求比较高，所以不适合。我使用的是原位操作的方法，先只在偶数位上找出不为偶数的元素，然后在奇数位上找出为偶数的元素，两者交换位置。最后两个
索引都必须加2.
"""
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 复杂版
        # length = len(A)
        # i, j = 1, 0
        # while j < length:
        #     if A[j] % 2 == 0:
        #         j += 2
        #         continue
        #     while i < length:
        #         if A[i] % 2 == 0:
        #             A[i], A[j] = A[j], A[i]
        #             j += 2
        #             i += 2
        #             break
        #         i += 2
        # return A

        # 简化版
        length = len(A)
        j = 1
        for i in range(0, length, 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[j], A[i] = A[i], A[j]
        return A

solve = Solution()
A = [2,0,3,4,1,3]
print(solve.sortArrayByParityII(A))