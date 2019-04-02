"""
本题是关于构造计算器的。表达式中有括号，加减号。没有乘除。位移要注意的是括号外面如果是减号的话，要注意括号里的符号要变号。
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        listNum = []
        length = len(s)
        # listOp = []
        # i = 0
        # while i < length:
        #     if s[i] in '(-+':
        #         if listOp == []:
        #             listOp.append(s[i])
        #         elif (s[i] == '(' and listOp[-1] in '(+-') or (s[i] in '+-' and listOp[-1] == '('):
        #             listOp.append(s[i])
        #         else:
        #             if listOp[-1] == '-':
        #                 listNum[-1] = listNum[-2] - listNum.pop()
        #             else:
        #                 listNum[-1] = listNum[-2] + listNum.pop()
        #             listOp[-1] = s[i]
        #     elif s[i] == ')':
        #         if listOp[-1] == '(':
        #             del listOp[-1]
        #         else:
        #             if listOp[-1] == '-':
        #                 listNum[-1] = listNum[-2] - listNum.pop()
        #             else:
        #                 listNum[-1] = listNum[-2] + listNum.pop()
        #             del listOp[-2:]
        #     elif s[i].isdigit():
        #         num = int(s[i])
        #         while i + 1 < length and s[i+1].isdigit():
        #             num = num * 10 + int(s[i+1])
        #             i += 1
        #         listNum.append(num)
        #     i += 1
        # if len(listNum) > 1:
        #     return listNum[-2] + listNum[-1] if listOp[0] == '+' else listNum[-2] - listNum[-1]
        # return listNum[0]

        # listNum = [0]
        # flag = True
        # i = 0
        # while i < length:
        #     if s[i].isdigit():
        #         num = int(s[i])
        #         while i + 1 < length and s[i+1].isdigit():
        #             num = num * 10 + int(s[i+1])
        #             i += 1
        #         if len(listNum) < 2:
        #             listNum.append(num)
        #         else:
        #             listNum[-1] = listNum[-1] + num if listNum.pop() == '+' else listNum[-1] - num
        #     elif s[i] == '(' and listNum != [] and listNum[-1] == '-':
        #         flag = False
        #     elif s[i] == '-':
        #         if len(listNum) > 0 and type(listNum[-1]) == str:
        #             listNum[-1] = '-' if listNum[-1] == '+' else '+'
        #         else:
        #             listNum.append('-' if flag else '+')
        #     elif s[i] == '+':
        #         if len(listNum) > 0 and type(listNum[-1]) == str:
        #             listNum[-1] = '-' if listNum[-1] == '-' else '+'
        #         else:
        #             listNum.append('+' if flag else '-')
        #     elif s[i] == ')':
        #         flag = True
        #     i += 1
        #     print(listNum)
        #
        # if type(listNum[0]) == str:
        #     return listNum[1] if listNum[0] == '+' else 0 - listNum[1]
        # return listNum[0]

        class Solution(object):
            def calculate(self, s):
                """
                :type s: str
                :rtype: int
                """
                length = len(s)
                listNum = [0]
                flag = True
                i = 0
                while i < length:
                    if s[i].isdigit():
                        num = int(s[i])
                        while i + 1 < length and s[i + 1].isdigit():
                            num = num * 10 + int(s[i + 1])
                            i += 1
                        if len(listNum) < 2:
                            listNum.append(num)
                        else:
                            listNum[-1] = listNum[-1] + num if listNum.pop() == '+' else listNum[-1] - num
                    elif s[i] == '(' and (s[i - 1] == '-'):
                        flag = not flag
                    elif s[i] in '+-':
                        if type(listNum[-1]) == str:
                            if (listNum[-1] == '-' and s[i] == '+') or (listNum[-1] == '+' and s[i] == '-'):
                                listNum[-1] = '-'
                            else:
                                del listNum[-1]
                        elif s[i] == '-':
                            listNum.append('-' if flag else '+')
                        elif s[i] == '+':
                            listNum.append('+' if flag else '-')
                    elif s[i] == ')':
                        flag = True
                    i += 1
                    print(listNum)

                return listNum[1] if len(listNum) > 1 else listNum[0]

        solve = Solution()
        # s = "2-4-(8+2-6+(8+4-(1)+8-10))"
        s = "(1+(4+5+2)-3)+(6+8)"
        print(solve.calculate(s))

solve = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
s = "-(-(+(-1)"
s = "2-(5-6)"
s = "-2+(5-6)"
print(solve.calculate(s))