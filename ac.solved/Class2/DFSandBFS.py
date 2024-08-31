# DFS와 BFS
# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

def solution():
    n, m, v = map(int, sys.stdin.readline().split())
    graph = {x:set() for x in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].add(y)
        graph[y].add(x)
    for dot in graph:
        graph[dot] = sorted(graph[dot], reverse=True)

    visited = set()
    dfs_Answer = []
    dfs_Stack = [v]
    while dfs_Stack:
        dot = dfs_Stack.pop()
        if dot not in visited:
            visited.add(dot)
            dfs_Answer.append(dot)
            for other in graph[dot]:
                if other not in visited:
                    dfs_Stack.append(other)

    visited.clear()
    bfs_Answer = []
    bfs_Queue = deque([v])
    while bfs_Queue:
        dot = bfs_Queue.popleft()
        if dot not in visited:
            visited.add(dot)
            bfs_Answer.append(dot)
            for other in reversed(graph[dot]):
                if other not in visited:
                    bfs_Queue.append(other)

    sys.stdout.write(' '.join(map(str, dfs_Answer)) + '\n' + ' '.join(map(str, bfs_Answer)) + '\n')

solution()