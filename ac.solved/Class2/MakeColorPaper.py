# 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys

def check_Filled(split):
    first_Color = split[0][0]
    for row in split:
        for element in row:
            if element != first_Color:
                return False
    return True

def paper_Split(paper, blue_Count=0, white_Count=0):
    if check_Filled(paper):
        if paper[0][0] == 1:
            return blue_Count + 1, white_Count
        else:
            return blue_Count, white_Count + 1

    mid = len(paper)//2

    top_Left = [row[:mid] for row in paper[:mid]]
    top_Right = [row[mid:] for row in paper[:mid]]
    bottom_Left = [row[:mid] for row in paper[mid:]]
    bottom_Right = [row[mid:] for row in paper[mid:]]

    splits = [top_Left, top_Right, bottom_Left, bottom_Right]
    for split in splits:
        blue_Count, white_Count = paper_Split(split, blue_Count, white_Count)

    return blue_Count, white_Count

def solution():
    n = int(sys.stdin.readline().strip())
    colorPaper = []
    for _ in range(n):
        colorPaper.append(list(map(int, sys.stdin.readline().split())))

    blue_Count, white_Count = paper_Split(colorPaper)
    sys.stdout.write(str(white_Count) + '\n' + str(blue_Count) + '\n')
solution()