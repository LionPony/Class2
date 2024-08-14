# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    sequence = [0 for j in range(10001)]

    for i in range(n):
        index = int(sys.stdin.readline().strip())
        sequence[index] += 1

    for i in range(len(sequence)):
        if sequence[i] != 0:
            for j in range(sequence[i]):
                print(i)

solution()