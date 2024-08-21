# 통계학
# https://www.acmicpc.net/problem/2108
import sys

def my_round(n):
    if n < 0:
        return -1 * my_round(n * -1)
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

def solution():
    n = int(sys.stdin.readline().rstrip())
    sequence = []
    for i in range(n):
        sequence.append(int(sys.stdin.readline().rstrip()))

    arithmetic_Mean = my_round(sum(sequence)/n)

    median = sorted(sequence)[n//2]

    frequency = {}
    for i in sequence:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    modeList = []
    for i in frequency.keys():
        if frequency[i] == max(frequency.values()):
            modeList.append(i)
    if len(modeList) >= 2:
        modeList.sort()
        mode = modeList[1]
    else:
        mode = modeList.pop()

    scope = abs(max(sequence) - min(sequence))
    sys.stdout.write(str(arithmetic_Mean) + '\n' + str(median) + '\n' + str(mode) + '\n' + str(scope))

solution()