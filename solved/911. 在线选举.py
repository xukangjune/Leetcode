"""
前面几个比我快的都是用了内置的二分查找，我的使用自己写的，所以慢一点，但是我除了开辟了一个cache就没有用其他的数据空间了，直接在self.persons上
改的。
"""
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.cache = {}
        self.persons = persons
        self.times = times
        self.n = len(self.times)
        self.calculate()

    def calculate(self):
        self.cache[self.persons[0]] = 1
        for i in range(1, self.n):
            if self.persons[i] not in self.cache:
                self.cache[self.persons[i]] = 0
            self.cache[self.persons[i]] += 1

            if self.cache[self.persons[i]] < self.cache[self.persons[i-1]]:
                self.persons[i] = self.persons[i-1]

    def binarySerach(self, time):
        left = 0
        right = self.n-1
        while left < right:
            mid = (left + right) >> 1
            if self.times[mid] == time:
                return self.persons[mid]
            elif self.times[mid] > time:
                right = mid - 1
            else:
                left = mid + 1
        return self.persons[right]


    def q(self, t):
        return self.binarySerach(t)

persons = [0,1,0,1,1]
times = [24,29,31,76,81]
solve = TopVotedCandidate(persons, times)
print(solve.persons)