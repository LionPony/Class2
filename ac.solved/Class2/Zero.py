# 제로
# https://www.acmicpc.net/problem/10773
import sys

def solution():
    k = int(sys.stdin.readline().rstrip())
    account = []
    for i in range(k):
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            account.pop()
        else:
            account.append(n)
    sys.stdout.write(str(sum(account)))

solution()