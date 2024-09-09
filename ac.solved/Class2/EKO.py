# 나무 자르기
# https://www.acmicpc.net/problem/2805
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = max(trees)
    while start < end:
        mid = (start + end) // 2
        lumber = sum(max(tree-mid,  0) for tree in trees)
        if lumber < m:
            end = mid
        else:
            start = mid + 1

    sys.stdout.write(str(end-1) + '\n')

solution()