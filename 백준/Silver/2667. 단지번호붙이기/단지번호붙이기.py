from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(houses, x, y):
    queue = deque([(x, y)])
    count = 1
    while queue:
        cx, cy = queue.popleft()
        houses[cx][cy] = 0
        for i in range(4):
            nx, ny = cx + direction[i][0], cy + direction[i][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if houses[nx][ny] == 0:
                continue
            if houses[nx][ny] == 1:
                houses[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
    return count


N = int(input())

houses = [list(map(int, input().strip())) for _ in range(N)]
cnt = []
for i in range(N):
    for j in range(N):
        if houses[i][j] == 1:
            cnt.append(bfs(houses, i, j))
cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)
