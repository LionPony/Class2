# ATM
# https://www.acmicpc.net/problem/11399
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    people = list(map(int, sys.stdin.readline().split()))
    people.sort()
    result = 0
    cumulate = 0
    for i in people:
        result += i + cumulate
        cumulate += i

    sys.stdout.write(str(result))

solution()