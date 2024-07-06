N = int(input())

def score(N):
    if 90 <= N <= 100:
        return 'A'
    elif 80 <= N <= 89:
        return 'B'
    elif 70 <= N <= 79:
        return 'C'
    elif 60 <= N <= 69:
        return 'D'
    else:
        return 'F'

print(score(N))