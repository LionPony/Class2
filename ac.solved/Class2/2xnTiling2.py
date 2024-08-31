# 2xn 타일링 2
# https://www.acmicpc.net/problem/11727
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    dp = [1, 3, 5]
    while len(dp) < n:
        dp.append(dp[-1]+(dp[-2]*2))
    
    sys.stdout.write(str(dp[n-1]%10007))

solution()