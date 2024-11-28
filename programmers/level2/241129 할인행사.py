from collections import Counter

def solution(want, number, discount):
    answer = 0

    arr = {}
    for x, y in zip(want, number):
        arr[x] = y

    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == arr :
            answer += 1
    return answer