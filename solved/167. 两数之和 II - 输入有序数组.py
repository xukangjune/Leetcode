"""
此题很经典，可以在首位设置索引，然后使用贪心算法，像中间汇集。
更快的方法是从头遍历，在没有解答之前将所有的值入字典，字典的查找是利用hash的，所以很快。
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        length = len(numbers)
        second = length - 1
        while first < second:
            temp = numbers[first] + numbers[second]
            if temp < target:
                first += 1
            elif temp > target:
                second -= 1
            else:
                return first+1, second+1


solve = Solution()
numbers = [2, 3, 4]
target = 6
print(solve.twoSum(numbers, target))

