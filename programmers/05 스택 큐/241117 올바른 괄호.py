# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        else :
            if arr :
                arr.pop()
            else :
                return False
    if arr:
        return False

    return True