# Hashing
# https://www.acmicpc.net/problem/15829
import sys

def solution():
    r = 1
    m = 1234567891

    l = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()

    answer = 0
    for i in range(l):
        answer += (ord(string[i])-96) * r
        r = r*31%m
        answer %= m
    
    print(answer)

solution()