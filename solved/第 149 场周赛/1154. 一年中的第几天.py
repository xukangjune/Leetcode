class Solution:
    def ordinalOfDate(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (y % 4 == 0):
            if (y % 100 == 0):
                if (y % 400 == 0):
                    days[1] = 29
            else:
                days[1] = 29

        return sum(days[:m-1])+d


solve = Solution()
# date = "2019-01-09"
# date = "2019-02-10"
date = "2004-03-01"
print(solve.ordinalOfDate(date))
