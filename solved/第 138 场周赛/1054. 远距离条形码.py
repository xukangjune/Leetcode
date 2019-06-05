class Solution:
    def rearrangeBarcodes(self, barcodes):
        length = len(barcodes)
        ret = [0] * length
        bag = set(barcodes)
        t = len(bag)
        times = {}
        for num in bag:
            times[num] = barcodes.count(num)
        tList = sorted(times.items(), key=lambda x:-x[1])

        # t = (length) // tList[0][1]
        print(t)

        barcodes.sort()

        i = 0
        j = i
        for num in barcodes:
            if j >= length:
                i += 1
                j = i
            ret[j] = num
            j += t

        return ret


solve = Solution()
a = [1,2,2]
print(solve.rearrangeBarcodes(a))