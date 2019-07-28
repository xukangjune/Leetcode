class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))


solve = Solution()
# address = "1.1.1.1"
# address = "255.100.50.0"
address = "...."
print(solve.defangIPaddr(address))