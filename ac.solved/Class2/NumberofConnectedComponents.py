# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
import sys
from collections import deque

def solution():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0
    visited = [False] * (n+1)
    for dot in range(1,n+1):
        if not visited[dot]:
            dots_Queue = deque([dot])
            visited[dot] = True

            while dots_Queue:
                current = dots_Queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        dots_Queue.append(neighbor)
            count += 1

    sys.stdout.write(str(count) + '\n')
solution()