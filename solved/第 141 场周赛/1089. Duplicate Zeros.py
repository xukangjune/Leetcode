class Solution:
    def duplicateZeros(self, arr) -> None:
        dumpy = arr[:]
        n = len(arr)
        i = 0
        j = 0
        while j < n:
            if dumpy[i] == 0:
                arr[j] = 0
                j += 1
                if j < n:
                    arr[j] = 0
            else:
                arr[j] = dumpy[i]
            i += 1
            j += 1


solve = Solution()
a = [0,0,0,0,0,1,1,0]
solve.duplicateZeros(a)
print(a)