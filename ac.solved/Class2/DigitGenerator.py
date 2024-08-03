# 분해합
# https://www.acmicpc.net/problem/2231
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    for i in range(1, n+1):
        digits = 0
        for j in str(i):
            digits += int(j)
        if i+digits == n:
            print(i)
            sys.exit()
    print('0')
    
solution()