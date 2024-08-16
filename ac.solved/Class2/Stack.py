# 스택
# https://www.acmicpc.net/problem/10828
import sys

class ArrayStack:
    def __init__(self):
        self.array = []
        self.sizeofArray = 0

    def push(self, x):
        self.array.append(x)
        self.sizeofArray += 1

    def pop(self):
        try:
            pop = self.array.pop()
            self.sizeofArray -= 1
            sys.stdout.write(pop + '\n')
        except:
            sys.stdout.write('-1\n')

    def size(self):
        sys.stdout.write(str(self.sizeofArray) + '\n')

    def empty(self):
        if self.sizeofArray == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
        
    def top(self):
        if self.sizeofArray == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.array[-1]) + '\n')

def solution():
    n = int(sys.stdin.readline().rstrip())
    arrayStack = ArrayStack()

    for i in range(n):
        command = sys.stdin.readline().split()
        if command[0] == 'push':
            arrayStack.push(command[1])
        elif command[0] == 'pop':
            arrayStack.pop()
        elif command[0] == 'size':
            arrayStack.size()
        elif command[0] == 'empty':
            arrayStack.empty()
        elif command[0] == 'top':
            arrayStack.top()        

solution()