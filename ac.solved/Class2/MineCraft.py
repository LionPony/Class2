# 마인크래프트
# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline
build_Time = 1
demolish_Time = 2

def solution():
    n, m, b = map(int, input().split())
    land = []
    for _ in range(n):
        land.extend(map(int, input().split()))
        
    min_Height = min(land)
    max_Height = min(max(land), (sum(land)+b)//(n*m))
    best_Time = float((sum(land)-(min_Height*m*n))*demolish_Time)
    best_Height = min_Height

    for target_Height in range(min_Height, max_Height+1):
        time = 0
        for height in land:
            if height > target_Height:
                time += (height - target_Height) * demolish_Time
            else:
                time += (target_Height - height) * build_Time
        if time <= best_Time:
            best_Time = time
            if target_Height > best_Height:
                best_Height = target_Height
    sys.stdout.write(f"{best_Time} {best_Height}\n")
solution()