# 블랙잭
# https://www.acmicpc.net/problem/2798
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    openCards = list(map(int, sys.stdin.readline().split()))
    
    combination = []
    for i in range(len(openCards)):
        for j in range(i+1, len(openCards)):
            for k in range(j+1, len(openCards)):
                combination.append(openCards[i]+openCards[j]+openCards[k])
    
    combination.sort()
    start = 0
    end = len(combination)-1
    while start <= end:
        mid = (start + end) // 2
        if combination[mid] == m:
            break
        elif combination[mid] < m:
            start = mid+1
        else:
            end = mid-1
    if combination[mid] <= m :
        print(combination[mid])
    else:
        print(combination[mid-1])

solution()