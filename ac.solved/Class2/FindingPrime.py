# 소수 찾기
# https://www.acmicpc.net/problem/1978
import sys
import math

def isPrime(a):
    if a == 1:
        return False
    for i in range(2, int(math.sqrt(a)+1)):
        if a%i == 0:
            return False
    return True

def solution():
    n = int(sys.stdin.readline().strip())
    sequence = map(int, sys.stdin.readline().split())
    
    answer = 0
    for i in sequence:
        if isPrime(i):
            answer += 1
    print(answer)

solution()