# 2xn 타일링
# https://www.acmicpc.net/problem/11726
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    dp = [1, 2, 3, 5]
    while len(dp) < n:
        dp.append(dp[-1]+dp[-2])
    sys.stdout.write(str(dp[n-1]%10007))

solution()