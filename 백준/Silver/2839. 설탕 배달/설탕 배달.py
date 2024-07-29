N = int(input())
result = -1

for i in range(N // 5, -1, -1):
    if (N - 5 * i) == 0:
        result = i
        break
    else:
        if (N - 5 * i) % 3 == 0:
            result = i + (N - 5 * i) // 3
            break

print(result)
