# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    array = []
    for i in range(n):
        array.append(int(sys.stdin.readline().strip()))
    array.sort()
    for i in array:
        print(i)

solution()