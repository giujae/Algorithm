def solution(brown, yellow):
    carpet_num = brown + yellow
    heights = []
    for i in range(3, int(carpet_num ** 0.5)+1):
        if carpet_num % i == 0:
            heights.append(i)
    for height in heights:
        width = carpet_num // height
        if (height - 2) * (width - 2) == yellow:
            return [width, height]