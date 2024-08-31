# Four Squares
# https://www.acmicpc.net/problem/17626
import sys
import math

def is_square(n):
    return int(math.sqrt(n))**2 == n

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    if is_square(n):
        sys.stdout.write("1")
        return

    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - i * i):
            sys.stdout.write("2")
            return
    
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i * i)) + 1):
            if is_square(n - i * i - j * j):
                sys.stdout.write("3")
                return
    
    sys.stdout.write("4")

solution()