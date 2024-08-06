# 평균
# https://www.acmicpc.net/problem/1546
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    scores = list(map(int, sys.stdin.readline().split()))
    maxScore = max(scores)

    adjustScores = []
    for i in scores:
        adjustScores.append((i / maxScore) * 100)
    
    print(sum(adjustScores)/len(adjustScores))

solution()