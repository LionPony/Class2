# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
import sys

def solution():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        k = int(sys.stdin.readline().strip())
        n = int(sys.stdin.readline().strip())

        apartment = [[0 for j in range(n+1)] for l in range(k+1)]
        for j in range(n+1):
            apartment[0][j] = j+1
        for j in range(k+1):
            apartment[j][0] = 1
        
        for j in range(1, k+1):
            for l in range(1, n):
                if apartment[j][l] == 0:
                    apartment[j][l] = apartment[j][l-1] + apartment[j-1][l]
        print(apartment[k][n-1])

solution()