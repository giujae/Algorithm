import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    oper_lst = [list(operation.split()) for operation in operations]
    for oper in oper_lst:
        order, num = oper
        if order == "I":
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        elif order == "D":
            if int(num) >= 0:
                if len(min_heap) == 0:
                    continue
                else:
                    max_value = -heapq.heappop(max_heap)
                    min_heap.remove(max_value)
                    heapq.heapify(min_heap)
            else:
                if len(min_heap) == 0:
                    continue
                else:
                    min_value = -heapq.heappop(min_heap)
                    max_heap.remove(min_value)
                    heapq.heapify(max_heap)
                    
    if len(min_heap) == 0:
            return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]