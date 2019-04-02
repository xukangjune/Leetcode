"""
遍历数组，检测每一位是否能够种花。首先，如果当前数字是0，则看后面的一位是否等于0.如果是0，就说明该位可以栽花，根据规则，下一个栽花的地方至少
是后面的两位；如果是1，那么当前位置不能栽花，接下来的可以栽花的位置至少后移三位。如果当前是1，那么直接后移两位。因为遍历的最后位置是数组的倒
数第二位，所以最后还要判断这两位是否可以栽花。
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        i = 0
        while i < length - 2:
            if flowerbed[i] == 0:
                if flowerbed[i+1] == 0:
                    count += 1
                    i += 2
                else:
                    i += 3
            else:
                i += 2
            continue
        print(count)
        return count >= n if flowerbed[length-1] == 1 or flowerbed[length-2] == 1 else count+1 >= n

solve = Solution()
# flowerbed = [1,0,0,0,0,1]
# flowerbed = [0,0,1,0,1]
flowerbed = [1,0,0]
print(solve.canPlaceFlowers(flowerbed, 1))