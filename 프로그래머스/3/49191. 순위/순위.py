def solution(n, result):
    answer = 0
    board = [[0] * (n + 1) for _ in range(n + 1)]

    for info in result:
        board[info[0]][info[1]] = 1
        board[info[1]][info[0]] = -1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if board[a][b] == 1 or board[b][a] == -1:
                    continue
                else:
                    if board[a][k] == board[k][b] == 1:
                        board[a][b] = 1
                        board[b][a] = -1
    for score in board:
        if score.count(0) == 2:
            answer += 1
    return answer