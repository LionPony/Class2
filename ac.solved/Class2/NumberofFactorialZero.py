# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
import sys

def solution():
    n = int(sys.stdin.readline())
    count_2 = 0
    count_5 = 0
    for i in range(1, n+1):
        while i > 1:
            if i % 2 == 0:
                count_2 += 1
                i //= 2
            elif i % 5 == 0:
                count_5 += 1
                i //= 5
            else:
                i = 0
    if count_2 <= count_5:
        print(count_2)
    else:
        print(count_5)

solution()