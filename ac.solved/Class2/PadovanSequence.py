# 파도반 수열
# https://www.acmicpc.net/problem/9461
import sys

def solution():
    t = int(sys.stdin.readline().rstrip())
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        while len(dp) < n:
            dp.append(dp[-1]+dp[-5])
        sys.stdout.write(str(dp[n-1]) + '\n')

solution()