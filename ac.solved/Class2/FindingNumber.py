# 수 찾기
# https://www.acmicpc.net/problem/1920
import sys

def solution():
    n = sys.stdin.readline().strip()
    array_A = set(sys.stdin.readline().split())
    m = sys.stdin.readline().strip()
    array_M = sys.stdin.readline().split()

    for i in array_M:
        if i in array_A:
            print('1')
        else:
            print('0')

solution()