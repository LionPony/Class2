# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
import sys

blackChessTile = []
for i in range(8):
    line = []
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                line.append('B')
            else:
                line.append('W')
        else:
            if j % 2 == 0:
                line.append('W')
            else:
                line.append('B')
    blackChessTile.append(line)

whiteChessTile = []
for i in range(8):
    line = []
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                line.append('W')
            else:
                line.append('B')
        else:
            if j % 2 == 0:
                line.append('B')
            else:
                line.append('W')
    whiteChessTile.append(line)

def errorCount(chessTile):
    countBlack = 0
    countWhite = 0
    for i in range(len(chessTile)):
        for j in range(len(chessTile[i])):
            if blackChessTile[i][j] != chessTile[i][j]:
                countBlack += 1

    for i in range(len(chessTile)):
        for j in range(len(chessTile[i])):
            if whiteChessTile[i][j] != chessTile[i][j]:
                countWhite += 1
    if countBlack > countWhite:
        return countWhite
    else:
        return countBlack

def solution():
    n, m = map(int, sys.stdin.readline().split())
    board = []
    for i in range(n):
        board.append(list(sys.stdin.readline().strip()))

    errors = []
    for i in range(n-7):
        chessTile = []
        for j in range(m-7):
            for k in range(i, i+8, 1):
                line = []
                for l in range(j, j+8, 1):
                    line.append(board[k][l])
                chessTile.append(line)
            errors.append(errorCount(chessTile))
            chessTile = []

    print(min(errors))

solution()