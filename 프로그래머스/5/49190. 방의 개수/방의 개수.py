from collections import defaultdict, deque


def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)
    visited = defaultdict(int)
    visited_dir = defaultdict(int)

    queue = deque([now])

    for i in arrows:
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)
            now = next

    now = queue.popleft()
    visited[now] = True

    while queue:
        next = queue.popleft()

        if visited[next]:
            if not visited_dir[(now, next)]:
                answer += 1
        else:
            visited[next] = True
            
        visited_dir[(now, next)] = True
        visited_dir[(next, now)] = True
        now = next
        
    return answer