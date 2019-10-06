'''
Welcome to vivo !
'''


def solution(N, M):
    ret = []
    people = [i for i in range(1, N+1)]
    cnt = 1
    i = 0

    while N != 0:
        if cnt % M == 0:
            ret.append(people[i])
            del people[i]
            if i == N-1:
                i = 0
            N -= 1
            cnt = 1
        else:
            cnt += 1
            i += 1
            if i == N:
                i = 0

    print(" ".join(map(str, ret)))

N, M = [int(i) for i in input().split()]
solution(N, M)