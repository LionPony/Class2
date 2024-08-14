# 단어 정렬
# https://www.acmicpc.net/problem/1181
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    words = []
    for i in range(n):
        word = sys.stdin.readline().strip()
        if word not in words:
            words.append(word)
    
    words.sort(key=lambda x: (len(x), x))

    for word in words:
        print(word)

solution()