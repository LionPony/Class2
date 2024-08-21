from collections import deque
import sys

def my_BFS(coins, k, current, count):
    queue = deque([(current, count)])
    visited = set([current])

    while queue:
        current, count = queue.popleft()

        if current == k:
            return count

        for coin in coins:
            next_value = current + coin
            if next_value <= k and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))

def solution():
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for i in range(n):
        coins.append(int(sys.stdin.readline().rstrip()))
    
    sys.stdout.write(str(my_BFS(coins, k, 0, 0)))

solution()