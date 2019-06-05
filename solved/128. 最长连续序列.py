"""
非常聪明的解法（别人的）。我自己写的是用C++写的并查集，先用字典来记录所有数字的共同祖先（祖先是数组中的一个坐标），祖先在数组中对应的就是长度。然后
在遍历nums中，先看num是否在prev内，然后看num-1和num+1分别在不在prev中，如果在，那么将左右数的祖先都迁移到左数中，这时候就要将右数的右数迁移（如果
有的话）。这样，还要考虑num-1和num+1中只有一个存在的情况。
但后来提交的时候，看到别人的解法觉得非常好。他其实也是并查集的概念，但是用的非常巧妙。首先遍历nums，如果num在prev就跳过。如果不在，那么看num-1和
num+1是否在，在就将left和right赋上相对应的长度，如果不在就是0。然后当前的长度就是left+right+1。下面一步很厉害，将prev[num-left]和
 prev[num+right]全部赋予temp长度。这时候在[left, right]这个闭区间都是temp，所以下次只要考虑left和right在prev中的值就行了。这之间的数虽然
 都是原来的长度，但是后面不会考虑到（因为遇到就直接跳过了）。厉害！！
"""
class Solution:
    def longestConsecutive(self, nums) -> int:
        prev = {}
        ret = 1
        for num in nums:
            if num in prev:
                continue
            left = prev[num-1] if num-1 in prev else 0
            right = prev[num+1] if num+1 in prev else 0
            temp = left + right + 1
            ret = max(temp, ret)
            prev[num-left] = temp
            prev[num+right] = temp
            prev[num] = temp
        print(prev)
        return ret


solve = Solution()
a = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2]
print(solve.longestConsecutive(a))