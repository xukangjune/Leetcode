class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = [0] * 26
        n = len(tiles)
        dict = {}
        for char in tiles:
            letters[ord(char)-65] += 1

        print(letters)


solve = Solution()
a = "AAB"
print(solve.numTilePossibilities(a))