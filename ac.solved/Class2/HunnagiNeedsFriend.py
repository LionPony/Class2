# 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    n, m = map(int, input().split())
    campus = [list(input().rstrip()) for _ in range(n)]

    I = None
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                I = (i, j)
                break

    locations_BFS = deque([I])
    visited = [[False] * m for _ in range(n)]
    visited[I[0]][I[1]] = True
    friends_Count = 0

    while locations_BFS:
        cX, cY = locations_BFS.popleft()
        for dX, dY in direction:
            nX, nY = cX + dX, cY + dY
            if 0 <= nX < n and 0 <= nY < m and not visited[nX][nY]:
                if campus[nX][nY] != 'X':
                    visited[nX][nY] = True
                    locations_BFS.append((nX, nY))
                    if campus[nX][nY] == 'P':
                        friends_Count += 1

    sys.stdout.write(f"{friends_Count}\n" if friends_Count > 0 else "TT\n")

solution()