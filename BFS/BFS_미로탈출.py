from collections import deque

def BFS(s, e, maps):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    ch = [[0] * m for _ in range(n)]
    dQ = deque()

    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                dQ.append((i, j, 0))
                ch[i][j] = 1

    while dQ:
        y, x, dis = dQ.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X' and ch[ny][nx] == 0:
                dQ.append((ny, nx, dis + 1))
                ch[ny][nx] = 1
                if maps[y][x] == e:
                    return dis + 1

    return -1

def solution(maps):
    res1 = BFS('S', 'L', maps)
    res2 = BFS('L', 'E', maps)
    if res1 == -1 or res2 == -1:
        return -1
    else:
        return res1 + res2


if __name__ == '__main__':
    # n = 3
    # maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
    maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
    print(solution(maps))