class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in range(1, 11):
            dict[str(i)] = 1
        for i in range(0, 10):
            dict['0'+str(i)] = 0
        for i in range(11, 27):
            dict[str(i)] = 2
        dict[str(20)] = 1
        for i in range(27, 100):
            dict[str(i)] = 1
        for i in [0, 30, 40, 50, 60, 70, 80, 90]:
            dict[str(i)] = 0
        print(dict)
        if len(s) < 3:
            return dict[s]
        else:
            for i in range(-3, -len(s)-1, -1):
                if s[i] == '0':
                    dict[s[i:]] = 0
                else:
                    if s[i:i+2] > '26':
                        dict[s[i:]] = dict[s[i+1:]]
                    else:
                        dict[s[i:]] = dict[s[i+1:]] + dict[s[i+2:]]
        return dict[s]



solve = Solution()
print(solve.numDecodings('0'))
print(solve.numDecodings('4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948'))