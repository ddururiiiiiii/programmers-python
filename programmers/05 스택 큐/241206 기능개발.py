import math
def solution(progresses, speeds):
    answer = []
    arr = []

    for i in range(len(progresses)):
        arr.append(math.ceil((100 - progresses[i]) / speeds[i]))

    for i in range(len(arr)):
        if i != 0:
            if arr[i-1] > arr[i]:
                arr[i] = arr[i-1]

    tmp = list(dict.fromkeys(arr))

    for i in tmp:
        answer.append(arr.count(i))
    return answer