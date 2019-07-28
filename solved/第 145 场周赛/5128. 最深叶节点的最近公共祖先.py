class Solution:
    def longestWPI(self, hours) -> int:
        ret = 0
        big = 0
        small = 0
        count = 0
        for num in hours:
            if num > 8:
                big += 1
                ret = big + small if big + small > ret else ret
            else:
                small += 1
                if small == big or big == 0:
                    big = small = 0
                else:
                    ret = big + small if big + small > ret else ret
        return ret


solve = Solution()
hours = [9,9,6,0,8,6,6,9]
# hours = [9,1,1]
print(solve.longestWPI(hours))