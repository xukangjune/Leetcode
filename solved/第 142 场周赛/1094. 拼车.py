from collections import defaultdict
class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        up = defaultdict(int)
        down = defaultdict(int)
        for i,  trip in enumerate(trips):
            up[trip[1]] += trip[0]
            down[trip[2]] += trip[0]

        num = 0
        for j in range(0, 1000):
            num += up[j]
            num -= down[j]
            if num > capacity: return False
        return True


solve = Solution()
# trips = [[2,1,5],[3,3,7]]
# capacity = 4
# trips = [[2,1,5],[3,3,7]]
# # capacity = 5
# trips = [[2,1,5],[3,0,7]]
# capacity = 3
trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
print(solve.carPooling(trips, capacity))