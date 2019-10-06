'''
Welcome to vivo !
'''
ret = float("inf")

def dfs(stone_list, weight, half, count, target, idx):
    global ret
    tmp = weight + stone_list[idx]
    if abs(tmp - half) > ret:
        return
    else:
        if count + 1 == target:
            ret = min(ret, abs(tmp-half))
            return
        for i in range(idx + 1, len(stone_list)):
            dfs(stone_list, tmp, half, count+1, target, i)

def solution(stone_list):
    total = sum(stone_list)
    half = total // 2
    target = len(stone_list) // 2
    stone_list.sort()
    print(stone_list)
    dfs(stone_list, 0, half, 0, target, 0)
    return ret


stone_list = [int(i) for i in input().split()]
print(solution(stone_list))