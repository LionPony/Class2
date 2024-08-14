# 나이순 정렬
# https://www.acmicpc.net/problem/10814
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    
    clients = []
    for i in range(n):
        client = sys.stdin.readline().split()
        age, name = int(client[0]), client[1]
        clients.append((age, name))

    clients.sort(key=lambda x :x[0])    
    
    for client in clients:
        print(client[0], client[1])

solution()