# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
import sys

def solution():
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '.':
            break
        line = list(line.split('.')[0])

        parentheses = []
        pair = {')':'(', ']':'['}
        balance = True
        for i in line:
            if i == '(' or i == '[':
                parentheses.append(i)
            elif i == ')' or i == ']':
                try:
                    parenthesis = parentheses.pop()
                    if pair.get(i) != parenthesis:
                        balance = False
                        break
                except:
                    balance = False
                    break
        
        if len(parentheses) == 0 and balance:
            sys.stdout.write('yes' + '\n')
        else:
            sys.stdout.write('no' + '\n')

solution()