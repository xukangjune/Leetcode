class Solution:
    def mctFromLeafValues(self, arr) -> int:
        ret = 0
        while len(arr)>1:
            num1 = min(arr)
            i = arr.index(num1)
            if i == 0:
                left = float("inf")
            else:
                left = arr[i-1]
            if i == len(arr) - 1:
                right = float("inf")
            else:
                right = arr[i+1]
            num2 = min(left, right)
            ret += num1 * num2
            arr.pop(i)
        return ret



solve=Solution()
arr = [6,2,4]
# arr = [1,2,1,1,1,1,1]
# arr = [7, 12, 8, 10]
print(solve.mctFromLeafValues(arr))