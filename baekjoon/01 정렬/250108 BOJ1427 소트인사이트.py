# https://www.acmicpc.net/problem/1427
num = str(input())
arr = sorted([int(i) for i in num], reverse=True)
print(''.join(map(str, arr)))