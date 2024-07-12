def solution(answers):
    scores = []
    result = []
    sub_ans1 = [1, 2, 3, 4, 5] * (len(answers) // 5) + [1, 2, 3, 4, 5][:(len(answers) % 5)]
    sub_ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8) + [2, 1, 2, 3, 2, 4, 2, 5][:(len(answers) % 8)]
    sub_ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:(len(answers) % 10)]

    for sub in [sub_ans1, sub_ans2, sub_ans3]:
        cnt = 0
        for i in range(len(sub)):
            if sub[i] == answers[i]:
                cnt += 1
            else:
                pass
        scores.append(cnt)
    for i in range(len(scores)):
        if scores[i] == max(scores):
            result.append(i+1)
    return result