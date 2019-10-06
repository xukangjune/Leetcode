def joseph(num_of_people, count):
    people = [i for i in range(1, num_of_people+1)]
    cnt = 1
    i = 0

    while num_of_people != 1:
        """从列表中删除人， 使用一个计数专门来记住当前的报数"""
        if cnt % count == 0:
            print(people[i], " must be killed!")
            del people[i]
            if i == num_of_people-1:
                """这一步很重要，如果恰好删除的人是最后一个，那么将下一个报数的人放回到第一个，因为我这里不想用取余运算"""
                i = 0
            num_of_people -= 1
            cnt = 1
        else:
            cnt += 1
            i += 1
            """同样，因为不想用取余，所以如果i到了末尾，直接返回到最前面"""
            if i == num_of_people:
                i = 0

    print(people[0], " is alive!") 


joseph(41, 3)