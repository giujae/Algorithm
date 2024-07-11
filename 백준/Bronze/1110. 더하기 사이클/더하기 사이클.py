N = int(input())

initial_num = N
new_num  = -1
cnt = 0

while initial_num != new_num:
    if N < 10:
        new_num = (N * 10) + (0 + N)
        N = new_num
        cnt += 1
    else:
        new_num = (N % 10) * 10 + (((N // 10) + (N % 10)) % 10)
        N = new_num
        cnt += 1

print(cnt)