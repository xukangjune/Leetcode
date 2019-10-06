n, m = map(int, input().split(' '))
matrix = []
dict1 = {}
dict2 = {}
max1 = 0
for i in range(n):
    matrix.append(list(map(int, input().split(" "))))


if n==m==1:
    print(0)
else:
    ret = 0
    i = 0
    while i < n:
        currentLine = matrix[i]
        for j in range(0, m, 2):  # 取下标为偶数
            if currentLine[j] in dict1:
                dict1[currentLine[j]] += 1
            else:
                dict1[currentLine[j]] = 1

        for j in range(1, m, 2):
            if currentLine[j] in dict2:
                dict2[currentLine[j]] += 1
            else:
                dict2[currentLine[j]] = 1

        i += 1
        if i >= n:
            break

        currentLine = matrix[i]
        for j in range(1, m, 2):
            if currentLine[j] in dict1:
                dict1[currentLine[j]] += 1
            else:
                dict1[currentLine[j]] = 1

        for j in range(0, m, 2):
            if currentLine[j] in dict2:
                dict2[currentLine[j]] += 1
            else:
                dict2[currentLine[j]] = 1
        i += 1

    list1 = sorted(dict1.items(), key=lambda x: x[1])
    list2 = sorted(dict2.items(), key=lambda x: x[1])
    if list1[-1][0] != list2[-1][0]:
        ret = n * m - list1[-1][1] - list2[-1][1]
    else:
        if len(list1) == 1 or len(list2) == 1:
            if len(list1) == len(list2) == 1:
                ret = n * m - max(list2[-1][1], list1[-1][1])

            elif len(list1) != 1:
                ret = n * m - list2[-1][1] - list1[-2][1]

            elif len(list2) != 1:
                ret = n * m - list2[-2][1] - list1[-1][1]

        else:
            ret = min(n * m - list2[-1][1] - list1[-2][1], n * m - list2[-2][1] - list1[-1][1])
    print(ret)
