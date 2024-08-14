# 카드2
# https://www.acmicpc.net/problem/2164
import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline().strip())
    array = deque(x for x in range(1, n+1))
    while len(array) > 1:
        array.popleft()
        array.append(array.popleft())
    print(array.pop())

solution()