# 가위 바위 보?
# https://www.acmicpc.net/problem/4493
import sys
input = sys.stdin.readline

def solution():
    cases = {'RR': 0, 'RP': 2, 'RS': 1,
             'PR': 1, 'PP': 0, 'PS': 2,
             'SR': 2, 'SP': 1, 'SS': 0}
    
    t = int(input().rstrip())
    for _ in range(t):
        result = [0, 0, 0]
        
        c = int(input().rstrip())
        for _ in range(c):
            play = input().strip().replace(' ', '')
            result[cases.get(play)] += 1
        
        if result[1] > result[2]:
           sys.stdout.write('Player 1\n')
        elif result[1] == result[2]:
            sys.stdout.write('TIE\n')
        else:
            sys.stdout.write('Player 2\n')

solution()