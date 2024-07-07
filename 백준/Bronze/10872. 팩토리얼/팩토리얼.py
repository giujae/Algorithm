N = int(input())
base_num = 1
for i in range(1, N+1):
    if N == 0:
        break
    else:
        base_num *= i
print(base_num)