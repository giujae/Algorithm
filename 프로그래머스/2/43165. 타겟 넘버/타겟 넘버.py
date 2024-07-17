def solution(numbers, target):
    answer = 0

    def find_sum(idx, current_sum):
        nonlocal answer

        if idx == len(numbers):
            if current_sum == target:
                answer += 1
            return

        find_sum(idx + 1, current_sum + numbers[idx])
        find_sum(idx + 1, current_sum - numbers[idx])

    find_sum(0, 0)
    return answer