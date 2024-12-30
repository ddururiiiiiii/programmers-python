from collections import Counter

def solution(str1, str2):

    # 두 문자 모두 소문자로 만들기
    str1 = str1.lower()
    str2 = str2.lower()

    # 다중집합1 만들기
    arr1 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i] + str1[i+1])

    # 다중집합2 만들기
    arr2 = []
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i] + str2[i+1])

    Counter1 = Counter(arr1)
    Counter2 = Counter(arr2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    # 자카드 유사도 구하기
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter)/len(union) * 65536)

    return 65536