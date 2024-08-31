# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    sequence = list(map(int, sys.stdin.readline().split()))
    prefixSum = [0]
    for i in sequence:
        prefixSum.append(prefixSum[-1] + i)
    for k in range(m):
        i, j = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(prefixSum[j]-prefixSum[i-1]) + '\n')

solution()