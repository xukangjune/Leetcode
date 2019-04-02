"""
分组考虑即可，但是开始还是有简单一点的解法的，这需要更好的数学知识。
如果有重叠，那么min(g,c) - max(a,e)就是重叠部分的长度，宽度以此类推。
"""
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        length = 0
        width = 0
        if E >= C or G <= A:
            pass
        elif A >= E and C <= G:
            length = C - A
        elif E > A and G < C:
            length = G - E
        else:
            temp = sorted([A, C, E, G])
            length = temp[2] - temp[1]
        if F >= D or H <= B:
            pass
        elif B >= F and D <= H:
            width = D - B
        elif F > B and H < D:
            width = H - F
        else:
            temp = sorted([B, D, F, H])
            print(temp)
            width = temp[2] - temp[1]
        print(length, width)
        return (C - A) * (D - B) + (G - E) * (H - F) - length * width


solve = Solution()
print(solve.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
# print(solve.computeArea(-2,-2,2,2,1,1,3,3))