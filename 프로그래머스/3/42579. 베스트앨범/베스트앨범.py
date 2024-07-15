from collections import defaultdict

def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    genres_played = defaultdict(int)
    for idx, value in enumerate(zip(genres, plays)):
        genres_played[value[0]] += value[1]
        music[idx] = value
    genres_played = dict(sorted(genres_played.items(), key=lambda x: x[1], reverse=True))
    music = sorted(music.items(), key=lambda x: x[1][1], reverse=True)
    for genre in genres_played.keys():
        cnt = 0
        for idx, info in music:
            if genre == info[0] and cnt < 2:
                answer.append(idx)
                cnt += 1
    return answer