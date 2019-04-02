"""
我做了好长时间的解法，还没有别人的快。首先，我建立了两个栈，第一个栈是一个递增栈，里面存的都是A中递增的序列，第二个
栈与第一个同步增减，其中第一个数是在这个数之前的数组构成的组合的和（子问题），第二个数是存着在这个数之前比他还有大的数。
接下来遍历数组A，如果比栈顶元素大，直接入栈，加上这个数与之前数组成数组的和（num+stackData[-1][0]）。如果是小于，则比较复杂一点，因为前面比
它大的数与它组合都会取它的值，所以要统计在它之前的所有的大于它的数，即如果第一个栈栈顶元素大于它，那么第二个栈对应
的栈顶元素的第二个值也是大于该数的数个数(count+stackData[-1][1])。一直累加下去，直到栈顶的元素小于遍历到的值。
此时总共的数为count*num+stackData[-1][0]。

下面是我看到的另一种解法，比上面的快，占内存小。该方法首先也建立了一个递增栈。数组中的数如果大于栈顶元素就将下标入栈。
如果小于栈顶元素，那么从遍历到的元素（A[i]）算起,前面的元素只要比它大，那么和它组成的子集就得取它。这种方法给人直观
上的感觉就是从后向前找组合的。方程A[j] * (i - j) * (j - k)中i-j就是在j位置右边比他大的数（包括自己），j-k就是
j位置左边比他小的数（包括自己）。这样上面的结果就是A[j]所能影响的所有的子数组的和。为了让构造更简单，将原来的A前后
各加了0。前面的0是为了让A中的元素都能入栈，后面的0为了让最后的栈清空（想象A原来就是一个递增的数组，那么最后的0将会
计算所有的解果）。
"""
class Solution:
    def sumSubarrayMins(self, A):
        # 自己写的
        # ret = 0
        # stackNum = [0]
        # stackData = [[0,0]]
        # for num in A:
        #     count = 1
        #     if num > stackNum[-1]:
        #         totalSum = num + stackData[-1][0]
        #     else:
        #         while stackNum and stackNum[-1] >= num:
        #             count += stackData[-1][1]
        #             del stackData[-1]               # 这两个栈同时增加，同时减小
        #             del stackNum[-1]                # stackData第一个存的是包括这个数之前所有数组合的和，第二个数是记录在原数组“大于”该数的个数
        #         totalSum = num * count + stackData[-1][0]
        #     stackData.append([totalSum, count])
        #     stackNum.append(num)
        #     ret += totalSum
        # return ret % (10 ** 9 + 7)

        # 另一个答案，很厉害
        ret = 0
        stack = []
        A = [0] + A + [0]
        for i, num in enumerate(A):
            while stack and A[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1]
                ret += A[j] * (i - j) * (j - k)
            stack.append(i)
        return ret % (10 ** 9 + 7)



solve = Solution()
# A = [3,1,2,4]
# A = [3, 4, 5, 1, 2]
# A = [81,55,2]
# A = [71,55,82,55]
print(solve.sumSubarrayMins(A))