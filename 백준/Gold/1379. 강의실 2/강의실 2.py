import sys, heapq

N = int(input())

lec_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

room_use = [0 for _ in range(N + 1)]

room = []

for i in range(1, N + 1):
    heapq.heappush(room, i)

lec_info.sort(key=lambda x: (x[1], x[2]))

room_inuse = []

for idx, st, en in lec_info:
    while room_inuse and room_inuse[0][0] <= st:
        end, room_num = heapq.heappop(room_inuse)
        heapq.heappush(room, room_num)
    new_room = heapq.heappop(room)
    heapq.heappush(room_inuse, (en, new_room))
    room_use[idx] = new_room


print(max(room_use))

for i in room_use[1:]:
    print(i)
