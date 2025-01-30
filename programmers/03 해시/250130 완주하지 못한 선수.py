# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    completion.append("-")

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

    return answer