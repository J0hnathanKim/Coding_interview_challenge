#프로그래머스 게임맵 최단거리
import queue

def solution(maps):
    n = len(maps)-1
    m = len(maps[0])-1
        # 좌, 우, 상, 하
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = queue.Queue()
    q.put((0,0))
    while not q.empty():
        cy, cx = q.get()

        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if (0<=ny<=n) and (0<=nx<=m):
                if maps[ny][nx] == 1: # 막힌길(0)이 아니고, 처음 가본 길(1)이어야 함-> 또 갔던 길이라면 1이 아님.
                    q.put((ny, nx))
                    maps[ny][nx] = maps[cy][cx] + 1

    if maps[n][m] > 1:
        return maps[n][m]
    return -1
