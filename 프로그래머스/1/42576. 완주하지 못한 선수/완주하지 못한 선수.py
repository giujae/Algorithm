def solution(participant, completion):
    dict = {}
    sum_hash = 0
    for part in participant:
        dict[hash(part)] = part
        sum_hash += hash(part)
    for comp in completion:
        sum_hash -= hash(comp)
    return dict[sum_hash]