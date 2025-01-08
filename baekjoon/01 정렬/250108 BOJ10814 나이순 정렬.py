# https://www.acmicpc.net/problem/10814
N = int(input())
arr = [list(input().split(" ")) for i in range(N)]
arr.sort(key=lambda x:int(x[0]))
for a, b in arr:
    print(a, b)