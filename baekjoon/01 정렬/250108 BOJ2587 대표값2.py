# https://www.acmicpc.net/problem/2587
def medium(arr):
    n = len(arr)
    if n % 2 == 1: #홀수
        return arr[n//2]
    else:
        return (arr[n//2-1] + arr[n//2]) // 2

infos = [int(input()) for _ in range(5)]
print(sum(infos)//5)
print(sorted(infos)[2])
