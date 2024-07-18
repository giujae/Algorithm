from collections import deque


def bfs(S, X, Y):
    queue = deque(virus)
    count = 0
    while queue:
        if count == S:
            break
        for _ in range(len(queue)):
            prev, x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + direction[i][0], y + direction[i][1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if plate[nx][ny] == 0:
                    plate[nx][ny] = prev
                    queue.append((plate[nx][ny], nx, ny))
        count += 1
    return plate[X - 1][Y - 1]


N, K = map(int, input().split())

plate = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

virus = []

for i in range(N):
    for j in range(N):
        virus.append((plate[i][j], i, j))
virus.sort()
v = bfs(S, X, Y)

print(v)
