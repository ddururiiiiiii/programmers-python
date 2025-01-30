# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for cloth, types in clothes:
        dic[types] = dic.get(types, 0) + 1

    for types in dic:
        print(dic[types])
        answer *= (dic[types] + 1)

    return answer - 1