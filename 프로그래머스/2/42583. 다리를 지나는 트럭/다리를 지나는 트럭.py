from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    current_weight = 0
    while truck_weights:
        time += 1
        current_weight -= bridge.popleft()
        if current_weight + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            current_weight += truck_weights.popleft()
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time