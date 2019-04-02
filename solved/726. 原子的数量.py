class Solution(object):
    def __init__(self):
        self.dict = {}
        self.pos = 0
        self.length = 0
        self.formula = None

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.formula = formula
        self.length = len(formula)
        res = ''
        dictList = sorted(self.func().items())
        for i in dictList:
            res += i[0]
            if i[1] != 1:
                res += str(i[1])
        print(res)

    def func(self):
        dict = {}
        while self.pos < self.length:
            if self.formula[self.pos].isupper():
                if self.pos + 1 < self.length and self.formula[self.pos + 1].islower():
                    temp = self.formula[self.pos:self.pos+2]
                    self.pos += 2
                else:
                    temp = self.formula[self.pos:self.pos+1]
                    self.pos += 1
                temp_num = ''
                while self.pos < self.length and self.formula[self.pos].isdigit():
                    temp_num += self.formula[self.pos]
                    self.pos += 1
                temp_num = 1 if temp_num == '' else int(temp_num)

                if temp not in dict:
                    dict[temp] = temp_num
                else:
                    dict[temp] += temp_num
            elif self.formula[self.pos] == '(':
                self.pos += 1
                newDict = self.func()
                for key, value in newDict.items():
                    if key in dict:
                        dict[key] += value
                    else:
                        dict[key] = value
            elif self.formula[self.pos] == ')':
                self.pos += 1
                temp_num = ''
                while self.pos < self.length and self.formula[self.pos].isdigit():
                    temp_num += self.formula[self.pos]
                    self.pos += 1
                temp_num = 1 if temp_num == '' else int(temp_num)
                for key in dict.keys():
                    dict[key] *= temp_num
                return dict
        return dict


solve = Solution()
formula = "H2O"
solve.countOfAtoms(formula)
