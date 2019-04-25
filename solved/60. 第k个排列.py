"""
今天是和翠翠在一起的两周年，我给他送了花，她很开心。
首先用的递归，有一点要注意的是在算index时，k要减1（自己细细品），这也是我想了好久才想到的，之前的出错都是因为它。下面就比较好办了，本来这题可以用之
前做的全排列的方法来解，但是太死板了，这题明显可以用数学的方法，每个数放在其他数前面的种类是一样的，所以可以按照这点来不断的减小K值，这便是核心。
后来觉得递归有点过美酒将递归换成了迭代没思路是一样的，就是复杂一点，中间也有好多要注意的地方，比如k == allCombinations时，要将 str(nums[0])
加上，因为我新建了一个ret，所以要注意。
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 迭代
        allCombinations = 1
        for i in range(2, n):
            allCombinations *= i
        nums = [i for i in range(1, n+1)]
        ret = ''
        while True:
            if k == 1:
                return ret + ''.join(map(str, nums))
            if k == allCombinations:
                return ret + str(nums[0]) + ''.join(map(str, nums[:0:-1]))
            if k > allCombinations:
                index = (k-1) // allCombinations
                tempNum = nums.pop(index)
                ret += str(tempNum)
                k -= allCombinations * index
            else:
                ret += str(nums.pop(0))
            allCombinations //= (n - 1)
            n -= 1

        # 递归
        # def recursive(k, allCombinations, i, n):
        #     if k == 1:
        #         return
        #     if k > allCombinations:
        #         index = (k-1) // allCombinations
        #         tempNum = nums.pop(i+index)
        #         nums.insert(i, tempNum)
        #         recursive(k-allCombinations * index, allCombinations // (n-1), i+1, n-1)
        #     elif k < allCombinations:
        #         recursive(k, allCombinations // (n-1), i+1, n-1)
        #     else:
        #         nums[i+1:] = nums[-1:i:-1]
        #
        # recursive(k, allCombinations, 0, n)
        # return ''.join(map(str, nums))


solve = Solution()
# print(solve.getPermutation(9,54494))
print(solve.getPermutation(4, 2))