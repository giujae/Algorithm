T = int(input())
for tc in range(1, T + 1):
    R, S = map(str, input().split())
    R = int(R)
    result = ''
    for string in S:
        result += string * R
    print(result)