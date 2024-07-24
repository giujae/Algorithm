stairs = int(input())

score = [int(input()) for _ in range(stairs)]

if stairs < 3:
    print(sum(score))
else:
    dp = [0] * stairs
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max((score[0] + score[2]), (score[1] + score[2]))
    for i in range(3, stairs):
        dp[i] = max((dp[i - 3] + score[i - 1] + score[i]), (dp[i - 2] + score[i]))
    print(dp[-1])
