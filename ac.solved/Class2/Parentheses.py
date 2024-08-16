# 괄호
# https://www.acmicpc.net/problem/9012
import sys

def solution():
    t = int(sys.stdin.readline().strip())
    
    for i in range(t):
        line = list(sys.stdin.readline().strip())
        parenthesis = []
        balance = True
        for j in line:
            if j == '(':
                parenthesis.append(j)
            else:
                try:
                    parenthesis.pop()
                except:
                    balance = False
                    break
        
        if len(parenthesis) == 0 and balance:
            sys.stdout.write('YES' + '\n')
        else:
            sys.stdout.write('NO' + '\n')

solution()