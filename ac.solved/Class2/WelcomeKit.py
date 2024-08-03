# 웰컴 키트
# https://www.acmicpc.net/problem/30802
import sys

def solution():
    n = int(sys.stdin.readline())
    sizes = list(map(int, sys.stdin.readline().split()))
    t, p = map(int, sys.stdin.readline().split())

    tBundle = 0
    for i in range(len(sizes)):
        if sizes[i] > 0:
            tBundle += sizes[i]//t
            if sizes[i]%t != 0:
                tBundle += 1
    
    print(tBundle)
    print(n//p, n%p)

solution()