from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

queue = deque()


def bfs(x, y):
    start = (x, y)
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[N - 1][M - 1]


print(bfs(0, 0))
