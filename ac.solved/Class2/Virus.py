# 바이러스
# https://www.acmicpc.net/problem/2606
import sys

def solution():
    numberofComputers = int(sys.stdin.readline().rstrip())
    networkAddedComputers = int(sys.stdin.readline().rstrip())
    graphofComputers = {}
    for i in range(1, numberofComputers+1):
        graphofComputers[i] = set()

    for i in range(networkAddedComputers):
        start, end = map(int, sys.stdin.readline().split())
        graphofComputers[start].add(end)
        graphofComputers[end].add(start)

    computers = [True for x in range(numberofComputers+1)]
    virusComputers = []
    virusComputers.append(1)
    while len(virusComputers) > 0:
        virusComputer = virusComputers.pop()
        for i in graphofComputers[virusComputer]:
            if computers[i]:
                computers[i] = False
                virusComputers.append(i)
    
    count = 0
    for i in range(2, numberofComputers+1):
        if not computers[i]:
            count += 1
    sys.stdout.write(str(count))

solution()