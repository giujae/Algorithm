N, S = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0

def s_sum(idx, sub_sum):
    global cnt
    
    if idx >= N:
        return
    
    sub_sum += arr[idx]
    
    if sub_sum == S:
        cnt += 1
    
    s_sum(idx + 1, sub_sum)
    s_sum(idx + 1, sub_sum - arr[idx])
    
s_sum(0, 0)
print(cnt)