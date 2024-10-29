def dfs(numbers, target, idx, value):
    answer = 0
    
    if(idx == len(numbers)):
        if(value == target):
            return 1
        else:
            return 0
    
    answer += dfs(numbers, target, idx+1, value+numbers[idx])
    answer += dfs(numbers, target, idx+1, value-numbers[idx])
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    
    return answer