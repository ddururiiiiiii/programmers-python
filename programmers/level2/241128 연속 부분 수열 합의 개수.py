def solution(elements):
    answer = 0

    result = set()
    elementLen = len(elements)
    elements = elements * 2


    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j:i+j+1]))

    return len(result)