def solution(priorities, location):
    processes = []
    proceed = []
    for i in range(len(priorities)):
        processes.append(chr(ord('A') + i))
    target = processes[location]
    queue = [info for info in zip(processes, priorities)]
    while queue:
        process = queue.pop(0)
        if any(q[1] > process[1] for q in queue):
            queue.append(process)
        else:
            proceed.append(process)
    for idx, order in enumerate(proceed):
        if order[0] == target:
            return idx + 1