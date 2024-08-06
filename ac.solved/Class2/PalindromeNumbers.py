# 펠린드롬수
# https://www.acmicpc.net/problem/1259
import sys

def solution():
    end = False
    while end == False:
        n = sys.stdin.readline().strip()
        if n == '0':
            end = True
        else:
            if n[::-1] == n:
                print('yes')
            else:
                print('no')

solution()