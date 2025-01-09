# https://www.acmicpc.net/problem/1181
N = int(input())
arr = sorted(list(set([input() for _ in range(N)])), key=lambda x:(len(x),x))
for i in arr:
    print(i)