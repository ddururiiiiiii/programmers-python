# https://www.acmicpc.net/problem/1427
n = str(input())
arr = sorted([int(i) for i in n], reverse=True)
print(''.join(map(str, arr)))
