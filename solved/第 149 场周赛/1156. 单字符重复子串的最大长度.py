from collections import defaultdict
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        map = defaultdict(list)
        c = text[0]
        n = len(text)
        s = 0
        i = 1
        while i < n:
            if text[i] != c:
                map[c].append([s, i-1])
                s = i
                c = text[i]
            i += 1
        map[c].append([s, i-1])

        ret = 1
        for key, value in map.items():
            first = value[0]
            n = len(value)
            tmp = first[1]-first[0]+1
            if n > 1:
                tmp += 1

            for other in value[1:]:
                if other[0] == first[1]+2:
                    if n > 2:
                        tmp = max(tmp, other[1]-first[0]+1)
                    else:
                        tmp = max(tmp, other[1]-first[0])
                else:
                    if n > 1:
                        tmp = max(tmp, other[1]-other[0]+2)
                first = other
            ret = max(ret, tmp)
        print(map)
        return ret



solve = Solution()
# text = "aaabbaaa"
# text = "aaaaa"
# text = "abcdef"
# text = "ababa"
# text = "aaabaaa"
text = "bbababaaaa"
print(solve.maxRepOpt1(text))
