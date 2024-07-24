N = int(input())

game_board = [list(map(int, input().split())) for _ in range(N)]

path = [[0] * N for _ in range(N)]
direction = [(1, 0), (0, 1)]
path[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = game_board[i][j]
        if game_board[i][j] == 0:
            break
        for k in range(2):
            nx, ny = i + jump * direction[k][0], j + jump * direction[k][1]
            if 0 <= nx < N and 0 <= ny < N:
                path[nx][ny] += path[i][j]
print(path[N - 1][N - 1])
