from itertools import combinations

def solution(clothes):
    closet = {}
    possible = 1
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    for key, value in closet.items():
        combi = combinations(value, 1)
        possible *= (len(list(combi)) + 1)
    return possible - 1