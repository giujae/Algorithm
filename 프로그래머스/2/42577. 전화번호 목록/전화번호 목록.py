def solution(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        arr = ''
        for num in number:
            arr += num
            if arr in hash_map and number != arr:
                return False
    return True