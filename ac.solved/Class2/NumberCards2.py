# 숫자 카드 2
# https://www.acmicpc.net/problem/10816
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().split()
    nCardsCount = {}
    for i in line:
        if i not in nCardsCount:
            nCardsCount[i] = 1
        else:
            nCardsCount[i] += 1

    m = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().split()
    answer = []
    for i in line:
        answer.append(str(nCardsCount.get(i, 0)))

    sys.stdout.write(' '.join(answer))

solution()