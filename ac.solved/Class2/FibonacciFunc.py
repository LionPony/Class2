# 피보나치 함수
# https://www.acmicpc.net/problem/1003
import sys

def solution():
    fibonacciSequence = []
    fibonacciSequence.append((1, 0))
    fibonacciSequence.append((0, 1))

    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        if len(fibonacciSequence) < n+1:
            for j in range(n+1+len(fibonacciSequence)):
                f1 = fibonacciSequence[-1]
                f2 = fibonacciSequence[-2]
                fibonacciSequence.append(tuple(sum(x) for x in zip(f1, f2)))
        
        sys.stdout.write(' '.join(map(str, list(fibonacciSequence[n]))) + '\n')
        
solution()