N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

def compressor(N, arr):
    # 영상을 합산 할 변수
    temp = 0
    # 영상의 합
    for lst in arr:
        temp += sum(lst)
    # 영상이 모두 1로만 되어 있으면
    if temp == N ** 2:
        return '1'
    # 영상이 모드 0으로만 되어 있으면
    if temp == 0:
        return '0'
    # 0과 1이 섞여있는 경우
    # 결과는 괄호안에 묶어서
    result = '(' 
    # 왼쪽 위
    result += compressor(N//2, [elem[:N//2] for elem in arr[:N//2]])
    # 오른쪽 위
    result += compressor(N//2, [elem[N//2:] for elem in arr[:N//2]])
    # 왼쪽 아래
    result += compressor(N//2, [elem[:N//2] for elem in arr[N//2:]])
    # 오른쪽 아래   
    result += compressor(N//2, [elem[N//2:] for elem in arr[N//2:]])
    result += ')'
    
    return result

print(compressor(N, arr))