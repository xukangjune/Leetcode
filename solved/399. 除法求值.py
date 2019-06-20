"""
原本用的是数组，但是后来题目中的元素不去那是字母，这就尴尬了。后来用的字典，并且字典的值是列表，第一个是指向的父亲，第二个是父亲到儿子的商。这样无论
在计算那两个数除法时，先找到是否是同一个祖先，然后得到祖先到当前值得商，最后用两个商做除法，就可以得到最后的结果。
"""
class Solution:
    def calcEquation(self, equations, values, queries):
        conn = {}
        ret = []

        def findFather(i):
            multi = 1
            while conn[i][0] != i:
                multi *= conn[i][1]
                i = conn[i][0]
            return i, multi


        for i, equ in enumerate(equations):
            a, b = equ
            if a in conn:
                father_1, num_1 = findFather(a)
                num_2 = 1
                father_2 = b
                if b in conn:
                    father_2, num_2 = findFather(b)
                conn[father_2] = father_1, num_1 * values[i] / num_2
            else:
                conn[a] = [a, 1]
                num_2 = 1
                father_2 = b
                if b in conn:
                    father_2, num_2 = findFather(b)
                conn[father_2] = a, values[i] / num_2

        for query in queries:
            a, b = query
            if a in conn and b in conn:
                father_1, num_1 = findFather(a)
                father_2, num_2 = findFather(b)
                if  father_1 == father_2:
                    ret.append(num_2 / num_1)
                    continue
            ret.append(-1.0)

        return ret




solve = Solution()
# equations = [ ["a", "b"], ["b", "c"], ["b", "e"], ["f", "g"], ["c", "g"]]
# values = [2.0, 3.0, 4.0, 1.5, 2]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"], ["a", "b"], ["f", "a"] ]
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(solve.calcEquation(equations, values, queries))