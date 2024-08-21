# solved.ac
# https://www.acmicpc.net/problem/18110
import sys

def roundUp(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

def solution():
    n = int(sys.stdin.readline().rstrip())
    trim = roundUp(n*15/100)

    scores = []
    for i in range(n):
        scores.append(int(sys.stdin.readline().rstrip()))
    scores.sort()

    trimmed_Scores = scores[trim:len(scores)-trim]
    if len(trimmed_Scores) > 0:
        trimmed_Average = str(roundUp(sum(trimmed_Scores) / len(trimmed_Scores)))
    else:
        trimmed_Average = '0'
    sys.stdout.write(trimmed_Average)

solution()