N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "-":
            if j == 0 or graph[i][j - 1] != "-":
                count += 1
        elif graph[i][j] == "|":
            if i == 0 or graph[i - 1][j] != "|":
                count += 1
print(count)