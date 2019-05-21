def quickSortCore(nums, n,  i, j):
    if i >= j:
        return
    pivot = nums[i]
    l = i + 1
    r = j
    while True:
        while r >= l and nums[r] >= pivot:
            r -= 1
        while r > l and nums[l] < pivot:
            l += 1
        if l >= r:
            break
        nums[l], nums[r] = nums[r], nums[l]
    nums[i], nums[r] = nums[r], nums[i]
    quickSortCore(nums, n, i, r-1)
    quickSortCore(nums, n, r+1, j)


def quickSort():
    nums = [1,22,32,32,1,34,6,2,23,32,1,2,44,-5,5,-4,0,23,-14,0,5,34,2,-1]
    quickSortCore(nums, len(nums)-1, 0, len(nums)-1)
    print(nums)

quickSort()