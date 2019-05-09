def move(n, a, b, c):        # 将a上面n个圆盘，通过b，全部移到c上去
    if n == 1:
        print("{} --> {}".format(a, c))
    else:
        move(n-1, a, c, b)   # 先将a上n-1个圆盘，通过c，移到b上
        print("{} --> {}".format(a, c))    # 这时候a上面只有一个圆盘，直接移到c上
        move(n-1, b, a, c)   # 最后将b上的n-1个圆盘，通过a，移到c上


move(7, 'a', 'b', 'c')