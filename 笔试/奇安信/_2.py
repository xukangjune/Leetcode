#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
from collections import defaultdict


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def max_length_substring(s):
    ret = 0
    map = defaultdict(int)
    start = 0
    for i, c in enumerate(s):
        if c in map:
            ret = max(ret, i-start)
            start = max(map[c]+1, start)
        map[c] = i
    ret = max(ret, len(s)-start)
    return ret



# ******************************结束写代码******************************


try:
    _s = input()
except:
    _s = None

res = max_length_substring(_s)

print(str(res) + "\n")