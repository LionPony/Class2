# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    array = [True for x in range(n)]

    count_K = 0
    index = 0
    answer = []
    while True in array:
        if array[index] == True:
            count_K += 1
        if count_K == k:
            answer.append(str(index+1))
            array[index] = False
            count_K = 0
        index += 1
        if index >= n:
            index %= n

    print('<', ', '.join(answer), '>', sep='')

solution()