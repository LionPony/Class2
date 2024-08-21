# 동전 0
# https://www.acmicpc.net/problem/11047
import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for i in range(n):
        coins.append(int(sys.stdin.readline().rstrip()))

    count = 0
    for i in reversed(coins):
        if k == 0:
            break
        count += k//i
        k %= i
    
    sys.stdout.write(str(count))

solution()