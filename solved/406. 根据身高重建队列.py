"""
这是一道典型的贪心算法。刚开始我写的是否受到了提示的影响，先将最矮的先排好。这样我还建立了一个代表索引的辅助数组，
这个辅助数组有特殊的含义，数组中的元素代表着返回数组中的空位置，不是空的位置说明已经排好了矮个子，这些人对后面的高个子没有影响。
所以后面排的只要注意这些空位置就行了。如果在辅助数组中第i个元素代表的空位置上插入人，说明在这个空位置前面应该有i个
高于或等于他的人。此外，如果两人相等身高，我引入了一个count来计数。

另一种解法是先排高个子，只要同等身高的有序站好，矮个子随便插入。所以先站最高的，接下来插入矮的，以第二个元素插入。
其实最主要的是同等身高的，同等身高看谁前面的人最少，最少的排前面，因为多的会将同等身高的计入在内。
"""
class Solution:
    def reconstructQueue(self, people):
        # 自己写的，有点差, 贪心是有的，不过太小
        # people.sort()
        # peopleInOrder = [None] * len(people)
        # restIndex = [i for i in range(len(people))]
        # prevPersonHeight = float("inf")
        # count = 0
        # for person in people:
        #     tempIndex = person[1]
        #     if person[0] == prevPersonHeight:
        #         count += 1
        #     else:
        #         count = 0
        #     tempIndex -= count
        #     rightIndex = restIndex[tempIndex]
        #
        #     del restIndex[tempIndex]
        #     peopleInOrder[rightIndex] = person
        #     prevPersonHeight = person[0]
        # return peopleInOrder

        # 别人的代码
        if not people:
            return []
        people.sort(reverse=True, key=lambda x: [x[0], -x[1]])
        print(people)
        res = [people[0]]
        for person in people[1:]:
            res.insert(person[1], person)
        return res



solve = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# people = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]
print(solve.reconstructQueue(people))