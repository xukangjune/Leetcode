class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lengthT = len(t)
        dictTimes = {}
        dictChars = {}
        for i in range(lengthT):
            if t[i] in dictChars:
                dictChars[t[i]].append(t[:i])
            else:
                dictChars[t[i]] = [t[:i]]
        for i in range(1, lengthT+1):
            dictTimes[t[:i]] = 0
        dictTimes[''] = 1
        print(dictTimes)
        print(dictChars)
        for char in s:
            if char in dictChars:
                for i in dictChars[char][::-1]:
                    print(i)
                    if dictTimes[i] > 0:
                        print(i+char)
                        dictTimes[i+char] += dictTimes[i]
        print(dictTimes)
        print(dictChars)
        return dictTimes[t]



solve = Solution()
# S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
# T = "bddabdcae"
# S = "babgbag"
# T = "bag"
S = 'rabbbit'
T = 'rabbit'
print(solve.numDistinct(S, T))