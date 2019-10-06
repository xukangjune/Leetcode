class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target: return 0
        