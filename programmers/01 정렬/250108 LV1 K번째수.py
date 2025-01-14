# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []

    for a, b, c in commands:
        list = array[a-1:b]
        list.sort()
        answer.append(list[c-1])
    return answer