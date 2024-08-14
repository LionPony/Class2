# 설탕 배달
# https://www.acmicpc.net/problem/2839
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    plasticBag = [5 for x in range(n//5)]
    while len(plasticBag) > 0:
        rest = n-sum(plasticBag)
        if rest % 3 == 0:
            print(rest//3 + len(plasticBag))
            sys.exit()
        else:
            plasticBag.pop()

    if n % 3 == 0:
        print(n//3)
    else:
        print(-1)
            
solution()