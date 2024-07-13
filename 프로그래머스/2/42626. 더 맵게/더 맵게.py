import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        merge = heapq.heappop(scoville) + (2 * heapq.heappop(scoville))
        heapq.heappush(scoville, merge)
        cnt += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return cnt