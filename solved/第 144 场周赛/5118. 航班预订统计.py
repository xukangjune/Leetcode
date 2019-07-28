"""
看的别人的解法，很厉害。
可以这么考虑，比如[1,2,10]，即1，2为10，下面介绍一个数组，这个数组中的数的意义是该位置上比前一个位置多的数量，比如[0,10,0,0,-10,0]。那么意思
就是位置1比位置0多10，位置2比位置1多0，位置4比位置3多-10.所以假设位置0的上的数为5，那么结果就是[5,15,15,15,5,5]。
所以我们对bookings中的每一个booking都可以生成这样一个辅助的数组。每个数组都是独立的，而且意义相同，所以可以合并到一起，这就是第一次遍历后的ret。
接下来遍历ret，因为位置0前面没有位置，所以他比前一个位置多的数就是初始值（前一个位置就是0）。然后依次向后累加得到最终的结果。
"""
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        ret = [0] * n
        for booking in bookings:
            ret[booking[0] - 1] += booking[2]
            if booking[1] < n:
                ret[booking[1]] -= booking[2]
        print(ret)
        for i in range(1, n):
            ret[i] += ret[i-1]
        return ret


solve = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(solve.corpFlightBookings(bookings, n))