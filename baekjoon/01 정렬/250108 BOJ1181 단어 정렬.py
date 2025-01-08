# https://www.acmicpc.net/problem/1181
N = int(input())
arr = [input() for i in range(N)]
arr = sorted(list(set(arr)), key=lambda x:(len(x),x))
for i in arr:
    print(i)