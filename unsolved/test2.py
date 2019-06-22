class Solution:
    def candy(self, ratings) -> int:
        prev = float("inf")
        ret = 0
        n = len(ratings)
        ratings = ratings + [float("inf")]
        i = 0
        start = 0
        while i < n-1:
            if ratings[i] < ratings[i+1]:
                while i < n-1 and ratings[i] < ratings[i+1]:
                    i += 1
                temp = i - start + 1
                ret +=(temp + 1) * temp // 2
                if prev == 1:
                    ret -= 1
                start = i
                prev = temp

            if i < n-1 and ratings[i] == ratings[i+1]:
                while i < n-1 and ratings[i] == ratings[i+1]:
                    i += 1
                if prev != float("inf") or prev == 1:
                    ret += (i - start)
                else:
                    ret += (i - start + 1)
                prev = 1
                start = i

            if i < n-1 and ratings[i] > ratings[i+1]:
                while i < n + 1 and ratings[i] > ratings[i+1]:
                    i += 1
                temp = i - start + 1
                if prev == 1:
                    ret += (temp + 1) * temp // 2 - 1
                elif prev == float("inf"):
                    ret += (temp + 1) * temp // 2
                else:
                    if temp > prev:
                        ret += (temp + 1) * temp // 2 - prev
                    else:
                        ret += (temp + 1) * temp // 2 - temp
                prev = 1
                start = i

        return ret


solve = Solution()
# a = [1,2,3,1,0]
# a = [1,2,87,87,87,2,1]
# a = [3,2,2,2,2,2,2,2,3]
a = [1]
print(solve.candy(a))