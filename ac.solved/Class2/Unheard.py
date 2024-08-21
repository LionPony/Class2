# 듣보잡
# https://www.acmicpc.net/problem/1764
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    unheard = set()
    for i in range(n):
        unheard.add(sys.stdin.readline().rstrip())

    unseeUnheard = []
    for i in range(m):
        unsee =sys.stdin.readline().rstrip()
        if unsee in unheard:
            unseeUnheard.append(unsee)

    unseeUnheard.sort()
    sys.stdout.write(str(len(unseeUnheard)) + '\n' + '\n'.join(unseeUnheard))

solution()