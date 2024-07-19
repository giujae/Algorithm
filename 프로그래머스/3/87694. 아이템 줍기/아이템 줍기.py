from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    coordinates = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in rectangle:
        x1, y1, x2, y2 = 2 * r[0], 2 * r[1], 2 * r[2], 2 * r[3]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    coordinates[i][j] = 0
                elif coordinates[i][j] != 0:
                    coordinates[i][j] = 1
    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

    queue = deque([(cx, cy)])

    while queue:
        cx, cy = queue.popleft()
        if cx == ix and cy == iy:
            answer = visited[cx][cy] // 2
            break

        for i in range(4):
            nx, ny = cx + directions[i][0], cy + directions[i][1]
            if coordinates[nx][ny] == 1 and visited[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] += visited[cx][cy]

    return answer