# 비밀번호 찾기
# https://www.acmicpc.net/problem/17219
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())

    sitePasswd = {}
    for i in range(n):
        site, passwd = map(str, sys.stdin.readline().split())
        sitePasswd[site] = passwd

    for i in range(m):
        site = sys.stdin.readline().rstrip()
        sys.stdout.write(sitePasswd[site] + '\n')
    return 0

solution()