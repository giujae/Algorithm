from collections import deque


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer


def bfs(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    while queue:
        b, cnt = queue.popleft()
        if b == target:
            break

        for i in range(len(words)):
            diff_cnt = 0
            if not visited[i]:
                for j in range(len(b)):
                    if b[j] != words[i][j]:
                        diff_cnt += 1
                if diff_cnt == 1:
                    queue.append((words[i], cnt + 1))
                    visited[i] = True
    return cnt
