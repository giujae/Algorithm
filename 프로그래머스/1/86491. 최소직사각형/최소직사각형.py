def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    max_width = 0
    max_height = 0
    
    for size in sizes:
        if size[0] > max_width:
            max_width = size[0]
        if size[1] > max_height:
            max_height = size[1]
    answer = max_height * max_width
    return answer