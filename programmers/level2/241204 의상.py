def solution2(clothes):
    dict = {}
    # 옷종류 : 갯수 ex) {'headgear': 2}
    for clothe, type in clothes:
        dict[type] = dict.get(type, 0) + 1

    answer = 1
    for type in dict:

        #모든 옷 종유에 대해서 안 입는 경우도 있기 때문에 +1을 해줌
        answer *= (dict[type] + 1)
        print(answer, dict[type] + 1)

    return answer - 1 #아무 것도 안입는 경우는 없으니 -1