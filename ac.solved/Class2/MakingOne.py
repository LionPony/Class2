# 1로 만들기
# https://www.acmicpc.net/problem/1463
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    sequence = {1:0}

    for i in range(2, n+1):
        sequence[i] = sequence[i-1] + 1
        if i % 2 == 0:
            sequence[i] = min(sequence[i], sequence[i//2]+1)
        if i % 3 == 0:
            sequence[i] = min(sequence[i], sequence[i//3]+1)

    sys.stdout.write(str(sequence[n]))

solution()