# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
import sys

def solution():
    parts = sys.stdin.readline().rstrip().split('-')
    sumofParts = []
    
    for part in parts:
        sumofParts.append(sum(map(int, part.split('+'))))
        
    answer = sumofParts[0] - sum(sumofParts[1:])

    sys.stdout.write(str(answer))
    
solution()