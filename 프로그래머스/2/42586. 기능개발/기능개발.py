from collections import deque

def solution(progresses, speeds):
    queue = deque([work for work in zip(progresses, speeds)])
    answer = []
    cnt = 0
    date = 0
    while len(queue) > 0:
        if (queue[0][0] + date * queue[0][1]) >= 100:
            queue.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            date += 1
    answer.append(cnt)
    return answer