class KMP():
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.pLength = len(p)
        self.sLength = len(s)
        self.next = [-1] * self.pLength

    def createNext(self):
        k = -1
        j = 0
        while j < self.pLength-1:
            if k == -1 or self.p[k] == self.p[j]:
                j += 1
                k += 1
                if self.p[k] == self.p[j]:
                    self.next[j] = self.next[k]
                else:
                    self.next[j] = k
            else:
                k = self.next[k]

    def matching(self):
        self.createNext()
        i = 0
        j = 0
        while i < self.sLength and j < self.pLength:
            if j == -1 or self.s[i] == self.p[j]:
                # 某种情况下，j== -1时，就会从头开始遍历P，并且s指针也要向后移动一位，所以 正好满足。
                i += 1
                j += 1
            else:
                j = self.next[j]


        if j == self.pLength:
            return i - j
        return -1


s = 'abcdcefdds'
p = 'ababab'
demo = KMP(s, p)
print(demo.matching())
print(demo.next)
