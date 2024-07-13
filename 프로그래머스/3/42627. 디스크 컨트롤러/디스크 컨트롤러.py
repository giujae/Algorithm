import heapq as hq

def solution(jobs):
    answer, now, i = 0, 0, 0
    heap = []
    start = -1
    jobs.sort()
    while i < len(jobs):
        for job in jobs[i:]:
            if start < job[0] <= now:
                hq.heappush(heap, job[::-1])
        if len(heap) > 0:
            current = hq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))