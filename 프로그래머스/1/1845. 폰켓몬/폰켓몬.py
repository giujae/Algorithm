from itertools import combinations

def solution(nums):
    poss_num = len(set(nums))
    num = len(nums)//2
    if poss_num > num:
        return num
    else:
        return poss_num