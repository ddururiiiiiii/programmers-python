# 첫번째 풀이
def solution1(s):
    arr = list(map(int, s.split(' ')))
    arr.sort()
    return str(arr[0]) + " " + str(arr[-1])

# 두번째 풀이
def solution2(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))