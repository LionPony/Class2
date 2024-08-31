# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
import sys

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for i in range(t):
        categories = {}
        disguises = int(sys.stdin.readline().rstrip())
        for j in range(disguises):
            name, category = map(str, sys.stdin.readline().split())
            if category not in categories:
                categories[category] = set()
            categories[category].add(name)

        count = 1
        for j in categories.keys():
             count *= len(categories[j]) + 1
        
        sys.stdout.write(str(count-1) + '\n')

solution()