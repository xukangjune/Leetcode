"""
本来自己写的快速排序，但是不够快，后来换了堆排序，快了很多。
自己对以前学的知识记忆不是很深刻，真好用这个机会复习了一下快速排序和堆排序。要经常复习！！！！
回到这一题，首先是快排，因为快排结束时，一定是找到了作为比较数的确切位置，所以而且大于此位置的数都比比较数大，反之亦然。所以就可以用这个比较数的位置和
需要找到数的位置比较（因为第k大，也就是排序好后，第n-1-k这个位置的数），就通过快排不断的缩小位置，直至比较数的位置正好等于所要求的位置。
其次是堆排，先用前k个数构建一个小顶堆，此时堆顶就是前k个数第k大的数（也就是最小的数），然后从第k+1个数开始，如果小于等于堆顶，跳过；大于，那么置换掉
堆顶，然后重构堆，将此时堆的最小值提取。最后的堆顶就是整个数组的第k大的数。
"""
class Solution:
    def findKthLargest(self, nums, k):
        # 堆排序
        minHeap = nums[:k]

        def adjustHeap(i):
            child = 2 * i + 1
            while child < k:
                if child + 1 < k and minHeap[child] > minHeap[child+1]:
                    child +=1
                if minHeap[child] >= minHeap[i]:
                    break
                minHeap[i], minHeap[child] = minHeap[child], minHeap[i]
                i = child
                child = 2 * i + 1

        for i in range((k-2) // 2, -1, -1):
            adjustHeap(i)

        for num in nums[k:]:
            if num > minHeap[0]:
                minHeap[0] = num
                adjustHeap(0)

        return minHeap[0]





        # 快速排序
        # def quickSort(l, r):
        #     pivot = nums[l]
        #     left = l + 1
        #     right = r
        #     while True:
        #         while right >= left and nums[right] >= pivot:
        #             right -= 1
        #         while right >= left and nums[left] < pivot:
        #             left += 1
        #         if (left >= right):
        #             break
        #         nums[right], nums[left] = nums[left], nums[right]
        #     nums[right], nums[l] = nums[l], nums[right]
        #     return right
        #
        # n = len(nums)
        # left = 0
        # right = n - 1
        # k = n - k
        # while True:
        #     ret = quickSort(left, right)
        #     if ret == k:
        #         return nums[ret]
        #     elif ret > k:
        #         right = ret-1
        #     else:
        #         left = ret+1

solve = Solution()
# nums = [3,2,1,5,6,4]
# nums = [3,2,3,1,2,4,5,5,6]
nums = [7,6,5,4,3,2,1]
print(solve.findKthLargest(nums, 2))