# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    array = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append([x, y])
    array.sort(key= lambda x : (x[1], x[0]))
    
    for element in array:
        print(element[0], element[1])

solution()