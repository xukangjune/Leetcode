from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1, arr2):
        map = defaultdict(int)
        rest = []
        for num in arr1:
            if num in arr2:
                map[num] += 1
            else:
                rest.append(num)
        ret = []
        for num in arr2:
            ret += [num] * map[num]
        ret += sorted(rest)
        return ret


solve = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,3,1,4,6,7,9,19]
print(solve.relativeSortArray(arr1, arr2))