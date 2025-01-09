# https://www.acmicpc.net/problem/2751
import sys
N = int(input())
arr = sorted([int(sys.stdin.readline())for _ in range(N)])
for i in arr:
    print(i)