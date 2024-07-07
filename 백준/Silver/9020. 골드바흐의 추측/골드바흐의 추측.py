T = int(input())

def find_prime(n):
    prime = [False, False] + [True] * (n - 1)
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return [k for k in range(n+1) if prime[k]]

for tc in range(T):
    
    n = int(input())

    filtered_list = find_prime(n)
    
    for prime_num in filtered_list:
        if prime_num <= (n // 2):
            if (n - prime_num) in filtered_list:
                min_diff = 10000
                diff = n - 2 * prime_num
                result = (0, 0)
                if diff < min_diff:
                    min_diff = diff
                    result = (prime_num, n - prime_num)

    print(result[0], result[1])