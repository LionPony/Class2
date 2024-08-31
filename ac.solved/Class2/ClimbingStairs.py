# 계단 오르기
# https://www.acmicpc.net/problem/2579
import sys

def solution():
    stairsN = int(sys.stdin.readline().rstrip())
    stairs = []
    for i in range(stairsN):
        stairs.append(int(sys.stdin.readline().rstrip()))

    maxStairs = []
    if stairsN == 1:
        maxStairs.append(stairs[0])
    elif stairsN == 2:
        maxStairs.append(stairs[0])
        maxStairs.append(stairs[0] + stairs[1])
    else:
        maxStairs.append(stairs[0])
        maxStairs.append(stairs[0] + stairs[1])
        maxStairs.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
        for i in range(3, stairsN):
            maxStairs.append(max(stairs[i] + maxStairs[i-2], stairs[i] + stairs[i-1] + maxStairs[i-3]))

    sys.stdout.write(str(maxStairs[stairsN-1]))

solution()