"""
终于用并查集做了一题，这题还是比较复杂的。首先用并查集将所给的节点分成几个集合。建立一个辅助数组，数组中数是下标
代表的节点指向的头节点位置，而头节点中的数是这个集合所包含的从整个节点的数目（数量以负数形式存储）。
这里有一个很重要的点，就是如果一个集合同时有两个点不感染的话，那么无论删除哪一个节点，整个集合到最后都会被感染。
所以，在给定的initial中（先排序），将头节点相同的节点删除（属于同一个集合），如果此时initial所有节点都被删除，
只要返回initial[0]。如果最后temp数组不为空，那么temp数组中每一个节点代表它所在的集合只有该节点被感染，删除该
节点后，这个集合就不会被感染了。所以最后只要比较temp数组中那个节点所在集合的总节点最多就行了，所以对每个节点先
找到头节点，头节点在nums中的数就是节点总数（注意是负数）。
"""
class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        n = len(graph)
        initial.sort()
        nums = [-1 for i in range(n)]
        def find(i):
            while nums[i] >= 0:
                nums[i] = find(nums[i])
                return nums[i]
            return i

        for i in range(n):
            for j in range(i+1, n):
                if graph[i][j]:
                    n1, n2 = find(i), find(j)
                    if n1 != n2:
                        nums[n1] += nums[n2]
                        nums[n2] = n1
        print("节点的指向： ", nums)

        bag = {}
        print('i: ', initial)
        for num in initial:
            key = find(num)
            if key in bag:
                bag[key].append(num)
            else:
                bag[key] = [num]

        ret = initial[0]
        total = 0
        print(bag)
        for key, value in bag.items():
            print(key, value)
            if len(value) == 1:
                temp = nums[find(key)]
                print("temp: ", temp)
                if temp < total:
                    ret = value[0]
                    total = temp
        return ret



solve = Solution()
# graph = [[1,1,0],[1,1,0],[0,0,1]]
# initial =
# graph = [[1,1,1],[1,1,1],[1,1,1]]
# initial = [1,2]
graph = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,1]]
initial = [5,0]
print(solve.minMalwareSpread(graph, initial))
