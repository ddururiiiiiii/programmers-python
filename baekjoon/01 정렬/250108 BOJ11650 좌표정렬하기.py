# https://www.acmicpc.net/problem/11650
# n = int(input())
# infos = [list(map(int, input().split())) for _ in range(n)]
# infos.sort()
# for a, b in infos:
#     print(a, b)
N = int(input())
arr = sorted([list(map(int, input().split(" "))) for _ in range(N)])
for a, b in arr:
    print(a, b)