def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        # print('num = ', num)
        for parent in leaves:
            # print('parent = ', parent, 'num = ', num)
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp

    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer