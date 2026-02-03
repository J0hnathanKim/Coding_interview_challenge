#프로그래머스 게임맵 최단거리
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append((ny, nx))

    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1