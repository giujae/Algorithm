import heapq

def solution(n, edge):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for vertex in edge:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist + 1 < distance[i]:
                distance[i] = dist + 1
                heapq.heappush(q, (dist+1, i))
    for i in distance:
        if i == max(distance[1:]):
            answer += 1
    return answer