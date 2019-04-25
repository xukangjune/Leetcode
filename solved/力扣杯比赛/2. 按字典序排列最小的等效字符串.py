class Solution:
    def smallestEquivalentString(self, A, B, S):
        nums = [i for i in range(26)]
        n = len(A)

        def all_set(target, i):
            if nums[i] != i:
                all_set(target, nums[i])
                nums[i] = target
            else:
                nums[i] = target


        def find_pre(i):
            if nums[i] == i:
                return i
            return find_pre(nums[i])

        for i in range(n):
            a = A[i]
            b = B[i]
            if find_pre(ord(a)-97) < find_pre(ord(b)-97):
                all_set(find_pre(ord(a)-97), ord(b)-97)
            else:
                all_set(find_pre(ord(b)-97), ord(a)-97)

        for i in range(26):
            pre = find_pre(i)
            if i != pre:
                nums[i] = pre

        ret = ''
        for char in S:
            ret += chr(nums[ord(char)-97]+97)
        print(nums)
        return ret


solve = Solution()
# A = "hello"
# B = "world"
# S = "hold"
A = "leetcode"
B = "programs"
S = "sourcecode"
print(solve.smallestEquivalentString(A,B,S))