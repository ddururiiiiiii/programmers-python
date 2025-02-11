# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

def solution(maps):
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 행과 열의 길이
    n, m = len(maps), len(maps[0])

    # BFS를 위한 큐 생성 (시작점 추가)
    queue = deque([(0, 0, 1)])  # (x좌표, y좌표, 현재까지 이동 거리)

    while queue:
        x, y, dist = queue.popleft()  # 큐에서 꺼냄

        # 도착 지점이면 최단 거리 반환
        if x == n - 1 and y == m - 1:
            return dist

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 안에 있고, 갈 수 있는 길이라면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))  # 다음 위치를 큐에 추가
                maps[nx][ny] = 0  # 방문 표시 (다시 방문 방지)

    return -1  # 도착할 수 없는 경우