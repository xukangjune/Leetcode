"""
本来想使用遍历来作为常规解法，没想到是最快的。从1开始遍历时，将每个数与前面的树比较，二u过大于它，继续遍历，如果等于直接返回False。
入宫小于，则跳出遍历。此时做一下判断，看姿势的位置是否是1，如果是，返回False（说明第一个数比第二个数大，不满足定义）。不是，则从这
个位置向后遍历，此时应该是严格递减的，所以一旦由数大于或等于前面的数，就返回False。否则一直遍历，遍历结束都没有出现问题，说明数组满
足题意，返回True。
"""
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 常规解法
        if len(A) < 3:
            return False
        num = A[0]
        temp = 1
        for i in range(1, len(A)):
            if A[i] > num:
                num = A[i]
            elif A[i] == num:
                return False
            else:
                temp = i
                break
        if temp == 1:
            return False
        for i in range(temp, len(A)):
            if A[i] < num:
                num = A[i]
            elif A[i] >= num:
                return False
        return True


solve = Solution()
A = [9,8,7,6,5,4,3,2,1,0]
print(solve.validMountainArray(A))
