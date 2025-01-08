def solution(array, commands):
    answer = []

    for a, b, c in commands:
        list = array[a-1:b]
        list.sort()
        answer.append(list[c-1])
    return answer