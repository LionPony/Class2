# 이항계수
# https://www.acmicpc.net/problem/11050
import sys

def makeCases(n, k, case, result):
    if len(case) == n:
        if case.count('1') == k:
            return result.append(case)
    else:
        makeCases(n, k, case+'0', result)
        makeCases(n, k, case+'1', result)
    
def solution():
    n, k = map(int, sys.stdin.readline().split())
    result = []
    makeCases(n, k, '', result)

    print(len(result))

solution()