def solution(numbers, target):
    answer = 0
    possible = [0]
    for num in numbers:
        tmp = []
        for poss in possible:
            tmp.append(poss + num)
            tmp.append(poss - num)
        possible = tmp
    for pos in possible:
        if pos == target:
            answer += 1
    return answer