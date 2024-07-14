from collections import deque

def solution(priorities, location):
    queue = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    cnt = 0
    while queue:
        process = queue.popleft()
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            cnt += 1
            if process[0] == location:
                return cnt