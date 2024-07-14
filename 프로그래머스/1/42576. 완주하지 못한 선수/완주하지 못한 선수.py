def solution(participant, completion):
    dict = {}
    for part in participant:
        dict[part] = dict.get(part, 0) + 1
    for comp in completion:
        dict[comp] -= 1
        if dict[comp] == 0:
            del dict[comp]
    return list(dict.keys())[0]