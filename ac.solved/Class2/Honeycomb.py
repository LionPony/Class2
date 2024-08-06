# 벌집
# https://www.acmicpc.net/problem/2292
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    
    honeycomb = 1
    count = 1
    while honeycomb < n:
        honeycomb += 6*count
        count += 1
    print(count)

solution()