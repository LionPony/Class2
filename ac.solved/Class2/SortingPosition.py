# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    
    array = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append([x, y])

    array.sort(key= lambda x: (x[0], x[1]))

    for i in array:
        print(' '.join(map(str, i)))

solution()