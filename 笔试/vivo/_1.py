'''
 Welcome to vivo !
'''

def solution(step_list):
    n = len(step_list)
    if n == 0:
        return -1
    elif n == 1:
        return 0
    else:
        dp = [n+1] * n
        dp[0] = 0
        for idx, num in enumerate(step_list):
            for i in range(idx+1, idx+num+1):
                if i < n:
                    dp[i] = min(dp[i], dp[idx]+1)
        if dp[-1] == n+1:
            return -1
        else:
            return dp[-1]


step_list = [int(i) for i in input().split()]
print(solution(step_list))