# https://school.programmers.co.kr/learn/courses/30/lessons/87946
import itertools

def solution(k, dungeons):
    answer = []
    dungeons_arr = list(itertools.permutations(dungeons, len(dungeons)))

    for dungeons in dungeons_arr:
        hp = k
        cnt = 0
        for dun in dungeons :
            if hp >= dun[0]:
                hp -= dun[1]
                cnt += 1
        answer.append(cnt)

    return max(answer)