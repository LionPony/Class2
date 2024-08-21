# 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys
from collections import deque

def solution():
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n, m = map(int, sys.stdin.readline().split())
        line = list(map(int, sys.stdin.readline().split()))
        printerQueue = deque()
        for j in range(n):
            printerQueue.append((line[j], j))
        maxList = sorted(line)

        count = 1
        while len(maxList) > 0:
            maxItem = maxList.pop()
            nowPrint = printerQueue.popleft()
            if nowPrint[0] < maxItem:
                printerQueue.append(nowPrint)
                maxList.append(maxItem)
            else:
                if nowPrint[1] == m:
                    sys.stdout.write(str(count) + '\n')
                    break
                count += 1

solution()