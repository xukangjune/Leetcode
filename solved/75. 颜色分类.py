"""
这一题其实就是对只拥有三个元素的数组排序，不用到额外的空间，并且时间复杂度为O（n）。下面先介绍我的写法。
首先，题目一个重要条件就是数组只有0，1，2三个元素，所以排序后，所有的元素0都在左边，2都在右边，1全部在中间。所以我们事前先定义了两个指针，
first，last。first指针用来放0，last指针用来放2。接下来，开始遍历数组，如果当前的值是0，先看当前位置是否与first相等，如果相等，说明该位置
之前全部都是0，所以不用变化，直接继续向后遍历，并且first加上1；如果当前位置大于first，那么说明first指针指的数不等于0（事实上只可能等于1，
因为当前位置之前的2都已经处理完了），这样的话交换当前位置的数和first指向的数，并且遍历位置与first都要加上1。第二种情况，如果当前位置是2，先
判断当前位置是否大于等于last，如果相等，那么就不用再处理了，直接中断遍历。如果不等，接着判断last的值是否等于2，如果等于的话，那么先将last减
去1，因为如果不这样做的话会将后面的2又引到前面了，本程序会陷入死循环。如果上述两个条件都不满足，就可以直接交换当前位置和last位置的数，注意，
此时还不能忙着先遍历下一个数，因为交换回来的可能是0，也是要处理的。如果遍历到的值是1，不用操作，接着向后遍历。PS：改变了一下遍历的边界，这样
如果当前位置等于last时，说明遍历就应该结束。
在别人提交的结果中看到了一种很棒的解法（如下），这种解法先扩展了数组的边界，lt是插入0的位置，gt是插入2的位置。在遍历的时候如果遇到0，那么
先将lt加1，然后进行交换；遇到1，先将gt减1，然后交换，遇到1不操作。这种方法的好处就是代码减少了，但是每次遇到0和1都要交换位置。

"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 双指针，第一个指针位置放0，第二个指针位置放2
        first = 0
        last = len(nums) - 1
        i = 0
        while i < last:
            if nums[i] == 0:
                if i > first:
                    nums[first], nums[i] = nums[i], nums[first]
                i += 1
                first += 1
            elif nums[i] == 2:
                if nums[last] != 2:
                    nums[last], nums[i] = nums[i], nums[last]
                last -= 1
            else:
                i += 1

        # 在解答中看到了另一种解法，很棒！！！
        # n = len(nums)
        # lt = -1
        # gt = n
        # i = 0
        #
        # while i < gt:
        #     if nums[i] == 0:
        #         lt += 1
        #         nums[lt], nums[i] = nums[i], nums[lt]
        #         i += 1
        #     elif nums[i] == 2:
        #         gt -= 1
        #         nums[gt], nums[i] = nums[i], nums[gt]
        #     else:
        #         i += 1


solve = Solution()
nums = [2,0,2,1,1,0]
solve.sortColors(nums)
print(nums)