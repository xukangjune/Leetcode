class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ret = ""
        curr = [0, 0]
        for char in target:
            k = ord(char) - 97
            i = k // 5
            j = k % 5
            x = i - curr[0]
            y = j - curr[1]
            if k != 25:
                if x > 0:
                    ret += 'D' * x
                else:
                    ret += 'U' * (-x)

                if y < 0:
                    ret += 'L' * (-y)
                else:
                    ret += 'R' * y

            else:
                ret += 'L' * (-y)
                ret += 'D' * x
            curr = [i, j]
            ret += '!'
        return ret


solve = Solution()
target = "tzbz"
print(solve.alphabetBoardPath(target))