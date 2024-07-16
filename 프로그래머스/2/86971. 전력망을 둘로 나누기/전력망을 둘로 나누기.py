from collections import defaultdict, deque

def bfs(cut_wire, n, wire_dict):
    count = 1
    visited = [False] * (n+1)
    visited[cut_wire[0]] = True
    queue = deque([cut_wire[0]])
    while queue:
        current = queue.popleft()
        for i in wire_dict[current]:
            if visited[i] or i == cut_wire[1]:
                continue
            else:
                count += 1
                queue.append(i)
                visited[i] = True
    return count

def solution(n, wires):
    answer = 100
    data = defaultdict(set)
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)
    for wire in wires:
        temp = bfs(wire, n, data)
        answer = min(answer, abs(n - temp - temp))
    return answer
