class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        positive =  filter(lambda x: x>0, A)
        print(positive)