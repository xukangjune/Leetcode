"""
看起来比较难，但是就是dfs，不过在深搜的过程中要做大量的剪枝，这样就能消除绝大多数情况。
"""
class Solution:
    def restoreIpAddresses(self, s: str):
        n = len(s)
        ret = []
        if n > 12 or n < 4:
            return ret

        def dfs(i, IP, count):
            if i == n and count == 4:
                ret.append(IP.lstrip('.'))
                return
            elif count == 4 or i == n:
                return
            if s[i] == '0':
                dfs(i+1, IP+'.0', count + 1)
            else:
                for j in range(1,4):
                    k = i + j
                    temp = s[i:k]
                    if k <= n and 0 <= int(temp) <= 255 and n - k <= (4-count-1)*3:
                        dfs(k, IP+'.'+s[i:k], count + 1)
            return

        dfs(0, '', 0)
        return ret


solve = Solution()
s = "25525511135"
# s = "010010"
print(solve.restoreIpAddresses(s))