N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

def compressor(N, arr):
    sum_lst = 0
    
    for lst in arr:
        sum_lst += sum(lst)

    if sum_lst == N ** 2:
        return '1'
    
    if sum_lst == 0:
        return '0'
    
    result = '('
    result += compressor(N//2, [h_arr[:N//2] for h_arr in arr[:N//2]])
    result += compressor(N//2, [h_arr[N//2:] for h_arr in arr[:N//2]])
    result += compressor(N//2, [h_arr[:N//2] for h_arr in arr[N//2:]])
    result += compressor(N//2, [h_arr[N//2:] for h_arr in arr[N//2:]])
    result += ')'
    
    return result

print(compressor(N, arr))