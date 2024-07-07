N = int(input())
numbers = list(map(int, input().split()))

prime = [2, 3]

for num in range(5, 1001, 2):
    for p_num in prime:
        if p_num * p_num <= num:
            if num % p_num == 0:
                break
    else:
        prime.append(num)

cnt = 0

for number in numbers:
    if number in prime:
        cnt += 1
print(cnt)