# 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
import sys
input = sys.stdin.readline
vowels = set(['a', 'e', 'i', 'o', 'u'])

def vowelTest(word):
    return any(letter in vowels for letter in word)

def continuousTest(word):
    vowelCount = consonantCount = 0
    for letter in word:
        if letter in vowels:
            vowelCount += 1
            consonantCount = 0
        else:
            consonantCount += 1
            vowelCount = 0
        
        if vowelCount == 3 or consonantCount == 3:
            return False
    return True

def continuousSameLetterTest(word):
    for i in range(1, len(word)):
        if word[i] == word[i-1] and word[i] not in {'e', 'o'}:
            return False
    return True

def solution():
    while True:
        word = input().rstrip()
        if word == 'end':
            break
        else:
            if vowelTest(word) and continuousTest(word) and continuousSameLetterTest(word):
                sys.stdout.write(f"<{word}> is acceptable.\n")
            else:
                sys.stdout.write(f"<{word}> is not acceptable.\n")

solution()