def solution(record):
    answer = []
    arr = []
    id = {}

    for v in record:
        arr = v.split(" ")
        if len(arr) == 3:
            id[arr[1]] = arr[2]

    for v in record:
        arr = v.split(" ")
        if len(arr) == 3 and arr[0] == 'Enter':
            answer.append(id[arr[1]] + '님이 들어왔습니다.')
        elif len(arr) == 2:
            answer.append(id[arr[1]] + '님이 나갔습니다.')

    return answer