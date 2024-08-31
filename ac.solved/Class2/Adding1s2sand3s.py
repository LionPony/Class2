# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
import sys

def solution():
    t = int(sys.stdin.readline().rstrip())
    dp = []
    dp.append(1)
    dp.append(2)
    dp.append(4)
    dp.append(7)
    
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        while len(dp) < n:
            dp.append(dp[-1]+dp[-2]+dp[-3])
        sys.stdout.write(str(dp[n-1]) + '\n')

solution()