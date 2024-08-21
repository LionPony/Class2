# 랜선 자르기
# https://www.acmicpc.net/problem/1654
import sys

def solution():
    k, n = map(int, sys.stdin.readline().split())
    my_LAN = []
    for i in range(k):
        my_LAN.append(int(sys.stdin.readline().rstrip()))
    longest = max(my_LAN)
    shortest = 1

    while shortest <= longest:
        mid = (shortest + longest)//2
        
        count = 0
        for i in my_LAN:
            count += i//mid
        
        if count >= n:
            shortest = mid+1
        else:
            longest = mid-1
    
    sys.stdout.write(str(longest))

solution()