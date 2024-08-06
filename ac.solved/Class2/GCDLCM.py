# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
import sys

def euclideanGCD(a, b):
    if b == 0:
        return a
    else:
        return euclideanGCD(b, a%b)

def solution():
    a, b = map(int, sys.stdin.readline().split())
    gcd = euclideanGCD(a, b)
    lcd = abs(a*b)//gcd

    print(gcd)
    print(lcd)

solution()