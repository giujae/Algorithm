from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(n, i, computers, visited)
            answer += 1
    return answer

def bfs(n, i, computers, visited):
    queue = deque([i])
    while queue:
        current = queue.popleft()
        visited[current] = True
        for j in range(n):
            if current != j and computers[current][j] == 1:
                if not visited[j]:
                    queue.append(j)