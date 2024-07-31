T = int(input())
for _ in range(T):
    N = int(input())
    zero, one = 1, 0
    for i in range(1, N + 1):
        zero, one = one, one + zero
    print(zero, one)
