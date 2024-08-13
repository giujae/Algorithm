import sys

N = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(N)]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = len(arr) // 2
    lower_arr = merge_sort(arr[:pivot])
    bigger_arr = merge_sort(arr[pivot:])

    merged_arr = []
    l = b = 0
    while l < len(lower_arr) and b < len(bigger_arr):
        if lower_arr[l] < bigger_arr[b]:
            merged_arr.append(lower_arr[l])
            l += 1
        else:
            merged_arr.append(bigger_arr[b])
            b += 1
    merged_arr += lower_arr[l:]
    merged_arr += bigger_arr[b:]
    return merged_arr


for num in merge_sort(numbers):
    print(num)
