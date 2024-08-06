# 스택 수열
# https://www.acmicpc.net/problem/1874
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    
    target = []
    for i in range(n):
        elementTarget = int(sys.stdin.readline().strip())
        target.append(elementTarget)

    stack = []
    answer = []

    target_iter = iter(target)
    target_now = next(target_iter, None)

    for i in range(1, n+1):
        stack.append(i)
        answer.append('+')
        while len(stack) > 0 and stack[-1] == target_now:
            stack.pop()
            answer.append('-')
            target_now = next(target_iter, None)

    if target_now != None:
        print('NO')
    else:
        for i in answer:
            print(i)

solution()