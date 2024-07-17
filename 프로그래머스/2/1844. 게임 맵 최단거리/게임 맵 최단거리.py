from collections import deque


def solution(maps):
    answer = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = bfs(direction, maps, 0, 0)

    if answer == 1:
        return -1
    else:
        return answer


def bfs(direction, maps, x, y):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + direction[i][0], cy + direction[i][1]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                queue.append((nx, ny))

    return maps[len(maps) - 1][len(maps[0]) - 1]