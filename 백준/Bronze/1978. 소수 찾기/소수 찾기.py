N = int(input())
numbers = list(map(int, input().split()))

def find_prime(numbers):
    cnt = 0
    prime = [2, 3]
    if max(numbers) == 1:
        return 0
    elif max(numbers) == 2:
        return 1
    elif max(numbers) == 3:
        if 2 in numbers:
            return 2
        else:
            return 1
    else:
        for num in range(5, max(numbers) + 1, 2):
            for p_num in prime:
                if p_num * p_num <= num:
                    if num % p_num == 0:
                        break
            else:
                prime.append(num)
                
    for number in numbers:
        if number in prime:
            cnt += 1
    return cnt

print(find_prime(numbers))
