"""
这题很简单呀，直接暴力解，但是我看前几名的写法都是这样呀！
首先要使用lambda函数进行排序，然后用返回数组存储第一个interval。接下来遍历数组（可以从第二个开始），如果当前interval的start大于
ret[-1]的end，说明不能合并，直接将interval加入ret；反之，说明能够合并，接着判断当前interval的end与ret[-1].end的关系，看是否会扩大
ret[-1].end。
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ret = [intervals[0]]
        for interval in intervals:
            if interval.start <= ret[-1].end:
                if interval.end > ret[-1].end:
                    ret[-1].end = interval.end
                else:
                    pass
            else:
                ret.append(interval)
        return ret