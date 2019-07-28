class Solution:
    def longestWPI(self, hours) -> int:
        def help(hours):
            ret = 0
            dummy = []
            big = small = 0
            start = 0
            j = 0
            count = 0
            while j < len(hours):
                if hours[j] <= 8:
                    count += 1
                    j += 1
                else:
                    break

            print(count)

            for i, num in enumerate(hours):
                if num > 8:
                    big += 1
                else:
                    small += 1
                    if small < big:
                        continue

                    if small == big:
                        if dummy and dummy[-1][1] == start - 1:
                            start = dummy[-1][0]
                            dummy.pop()
                        dummy.append([start, i])
                        big = 0
                    start = i + 1
                    small = 0


            if big > small:
                if dummy and dummy[-1][1] == start - 1:
                    start = dummy[-1][0]
                    dummy.pop()
                dummy.append([start, len(hours)])
            print(dummy)
            for period in dummy:
                temp = period[1] - period[0]
                if temp > ret:
                    ret = temp

            return ret

        ret1 = help(hours)
        ret2 = help(hours[::-1])

        return max(ret1, ret2)




solve = Solution()
# hours = [9,9,6,0,9,8,9,6,6,9,9,2,3,9,9,9]
# hours = [9,1,1]
# hours = [9,9,6,0,6,6,9]
# hours = [6, 6, 9]
# hours = [6,6,9,9,9]
hours = [8,12,7,6,10,10,9,11,12,6]
print(solve.longestWPI(hours))