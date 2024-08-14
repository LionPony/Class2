# FizzBuzz
# https://www.acmicpc.net/problem/28702
import sys

def solution():
    order = 0
    
    n1 = sys.stdin.readline().strip()
    n2 = sys.stdin.readline().strip()
    n3 = sys.stdin.readline().strip()
    
    ns = [n1, n2, n3]
    for i in ns:
        if i.isdigit():
            if i == n1:
                order = int(i)+3
            elif i == n2:
                order = int(i)+2
            else:
                order = int(i)+1
            break
    
    if order % 3 == 0 and order % 5 == 0:
        print('FizzBuzz')
    elif order % 3 == 0 and order % 5 != 0:
        print('Fizz')
    elif order % 3 != 0 and order % 5 == 0:
        print('Buzz')
    else:
        print(order)

solution()