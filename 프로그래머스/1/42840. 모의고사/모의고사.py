def solution(answers):
    sub_ans1 = [1, 2, 3, 4, 5]
    sub_ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sub_ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0] * 3
    
    result = []
    
    for i in range(len(answers)):
        if answers[i] == sub_ans1[i % len(sub_ans1)]:
            scores[0] += 1
        if answers[i] == sub_ans2[i % len(sub_ans2)]:
            scores[1] += 1
        if answers[i] == sub_ans3[i % len(sub_ans3)]:
            scores[2] += 1
    
    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx + 1)
    return result