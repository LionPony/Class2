# 좌표 압축
# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

def solution():
    n = int(input().rstrip())
    sequence = list(map(int, input().split()))
    sequenceNoDupSorted = sorted(list(set(sequence)))
    dict = {value: index for index, value in enumerate(sequenceNoDupSorted)}
    answer = [str(dict[num]) for num in sequence]
    sys.stdout.write(' '.join(answer) + '\n')

solution()