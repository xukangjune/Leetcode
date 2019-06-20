from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        n = len(values)
        index = [i for i in range(n)]
        index.sort(key=lambda i: values[i], reverse=True)
        count = 0
        ret = 0
        dumpy = defaultdict(int)
        for i in index:
            if dumpy[labels[i]] == use_limit:
                continue
            ret += values[i]
            dumpy[labels[i]] += 1
            count += 1
            if count == num_wanted:
                break
        return ret





solve = Solution()
values = [3,2,3,2,1]
labels = [1,0,2,2,1]
num_wanted = 2
use_limit = 1
print(solve.largestValsFromLabels(values, labels, num_wanted, use_limit))