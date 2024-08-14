# 덩치
# https://www.acmicpc.net/problem/7568
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    array = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append([x, y])

    answer = []
    for i in array:
        count = 1
        for j in array:
            if j[0] > i[0] and j[1] > i[1]:
                count += 1
        answer.append(count)
    
    answer = list(map(str, answer))
    print(' '.join(answer))

solution()