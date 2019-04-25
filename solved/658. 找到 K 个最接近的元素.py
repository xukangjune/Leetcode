"""
我只能做到这里了，排名第一的算法我看不懂，惭愧！！！
我的方法，先用二分法找到x应该在arr中的位置，然后左右开弓，不断的找最接近的数。其中，如果某一段到达边界，可以快速处理。
"""
class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        def binarySearch():
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        right = binarySearch()
        if right == n-1:
            return arr[n-k:]
        if right == 0:
            return arr[:k]

        ret = []
        left = right - 1
        count = 0
        while count < k:
            if x- arr[left] <= arr[right] - x:
                ret .insert(0, arr[left])
                left -= 1
            else:
                ret.append(arr[right])
                right += 1
            count += 1
            if left == -1:
                return ret + arr[right:right+k-count]
            if right == n:
                return arr[left+count+1-k:left+1] + ret
        return ret


solve = Solution()
arr = [1,2,3,4,5]
print(solve.findClosestElements(arr, 4, 3))