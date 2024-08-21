# 소수 구하기
# https://www.acmicpc.net/problem/1929
import sys
import math

def isPrime(n):
    if n == 1:
        return False
    else:
        goal = int(math.sqrt(n))+1
        for i in range(2, goal):
            if n % i == 0:
                return False
        return True

def solution():
    m, n = map(int, sys.stdin.readline().split())
    sieve = dict.fromkeys([x for x in range(m, n+1)], True)

    for i in range(m, n+1):
        if sieve.get(i):
            if isPrime(i):
                sys.stdout.write(str(i) + '\n')
                for j in range(i*2, n+1,i):
                    sieve[j] = False
            else:
                sieve[i] = False

solution()