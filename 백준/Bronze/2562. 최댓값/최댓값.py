numbers = []
for _ in range(9):
    numbers.append(int(input()))

def find_max(numbers):
    max_num = 0
    max_pos = 0
    for idx, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_pos = idx + 1
    print(max_num)
    print(max_pos)

find_max(numbers)