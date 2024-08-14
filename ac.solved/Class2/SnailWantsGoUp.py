# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869
import sys

def solution():
    a, b, v = map(int, sys.stdin.readline().split())
    
    day = (v-b)//(a-b)
    if (v-b)%(a-b) == 0:
        print(day)
    else:
        print(day+1)

solution()