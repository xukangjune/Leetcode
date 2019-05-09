"""
我自己写的其实是BFS+递归，每次都将每一层所有的情况全部找到，但是这样太耗时了，因为有的可能靠前的情况就已经满足要求了，靠后的情况不满足。所以，后来看
别人的事DFS+递归，就是每次只取一种情况，一直dfs下去，如果满足，那么后面的都不用考虑了，直接返回，如果这种情况不满足，那么回溯上一层的另一种情况。
"""
class Solution:
    def pyramidTransition(self, bottom, allowed):
        # 看网上的解法，DFS+递归
        bricks = {}
        for brick in allowed:
            if brick[0:2] not in bricks:
                bricks[brick[0:2]] = []
            bricks[brick[0:2]].append(brick[2])

        def dfs(bottom):
            n = len(bottom)
            if n == 1:
                return True
            for i in range(n-1):
                if bottom[i:i+2] not in bricks:
                    return False
            nextLevel = []
            findNext(bottom, 0, n, '', nextLevel)
            for item in nextLevel:
                if dfs(item):
                    return True
            return False

        def findNext(bottom, idx, n, temp, ret):
            if  idx == n-1:
                ret.append(temp)
                return
            for char in bricks[bottom[idx:idx+2]]:
                findNext(bottom, idx+1, n, temp+char, ret)
            return

        return dfs(bottom)



        # bfs迭代版本， 超时，没通过
        # bricks = {}
        # n = len(bottom)
        # for brick in allowed:
        #     if brick[0:2] not in bricks:
        #         bricks[brick[0:2]] = []
        #     bricks[brick[0:2]].append(brick[2])
        # print(bricks)
        # levels = [bottom]
        #
        # while levels:
        #     if n == 1:
        #         return True
        #     tempLevel = []
        #     for arrays in levels:
        #         prev = ['']
        #         for i in range(n-1):
        #             if arrays[i:i+2] in bricks:
        #                 currStr = []
        #                 for char in bricks[arrays[i:i+2]]:
        #                     for prev_char in prev:
        #                         currStr.append(prev_char + char)
        #                 prev = currStr
        #             else:
        #                 break
        #             if i == n-2:
        #                 tempLevel += prev
        #     levels = tempLevel
        #     n -= 1
        # return False

        # bfs递归版本，超时，没通过
        # bricks = {}
        # for brick in allowed:
        #     if brick[0:2] not in bricks:
        #         bricks[brick[0:2]] = []
        #     bricks[brick[0:2]].append(brick[2])
        # print(bricks)
        # level = [bottom]
        #
        # def dfs(i, length, string):
        #     ret = []
        #     if i < length:
        #         print(string[i:i+2])
        #         if string[i:i+2] in bricks:
        #             ans = dfs(i+1, length, string)
        #             if ans:
        #                 for j in ans:
        #                     for char in bricks[string[i:i+2]]:
        #                         ret.append([char] + j)
        #
        #             else:
        #                 return [[char] for char in bricks[string[i:i + 2]]]
        #     return ret
        #
        #
        # while level:
        #     print(level)
        #     tempLevel = []
        #     for k in level:
        #         n = len(k)
        #         if n == 1:
        #             return True
        #         for ans in dfs(0, n-1, ''.join(map(str, k))):
        #             if len(ans) == n-1:
        #                 tempLevel.append(ans)
        #         level = tempLevel
        # return False

solve = Solution()
# bottom = "XYZ"
# allowed = ["XYD", "YZE", "DEA", "FFF"]
# bottom = "XXYX"
# allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
bottom = "BDBBAA"
allowed = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
print(solve.pyramidTransition(bottom, allowed))