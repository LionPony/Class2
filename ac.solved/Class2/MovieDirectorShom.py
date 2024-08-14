# 영화감독 숌
# https://www.acmicpc.net/problem/1436
import sys

def solution():
    n = int(sys.stdin.readline())
    
    count = 0
    start = 666
    while count < n:
        if '666' in str(start):
            count += 1
        start += 1

    print(start-1)

solution()