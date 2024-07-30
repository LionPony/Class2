# 직각삼각형
# https://www.acmicpc.net/problem/4153
import sys

def solution():
    end = False
    while end == False:
        a, b, c = map(int, sys.stdin.readline().split())
        angles = [a, b, c]
        if a == 0 and b == 0 and c == 0:
            break
        else:
            angles.sort()
            if angles[0]**2+angles[1]**2 != angles[2]**2:
                print('wrong')
            else:
                print('right')

solution()