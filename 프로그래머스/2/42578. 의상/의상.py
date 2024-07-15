def solution(clothes):
    closet = {}
    for cloth, type in clothes:
        if type not in closet:
            closet[type] = 2
        else:
            closet[type] += 1
    possible = 1
    for value in closet.values():
        possible *= value
    return possible - 1