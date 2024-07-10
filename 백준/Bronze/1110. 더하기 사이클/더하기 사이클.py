N = int(input())

default = N
new_N = -1
cnt = 0

while N != new_N:
    if default < 10:
        sum_N = 0 + (default % 10)
        new_N = (default % 10) * 10 + (sum_N % 10)
        default = new_N
        cnt += 1
    else:
        sum_N = (default // 10) + (default % 10)
        new_N = (default % 10) * 10 + (sum_N % 10)
        default = new_N
        cnt += 1
print(cnt)