# 큐
# https://www.acmicpc.net/problem/10845
import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def push(self, x):
        if self.length == 0:
            self.head = Node(x)
            self.rear = self.head
            self.length += 1
        else:
            newNode = Node(x)
            self.rear.next = newNode
            self.rear = newNode
            self.length += 1

    def pop(self):
        if self.length == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.head.item) + '\n')
            self.head = self.head.next
            self.length -= 1

    def size(self):
        sys.stdout.write(str(self.length) + '\n')

    def empty(self):
        if self.length == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    def front(self):
        if self.length == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.head.item) + '\n')

    def back(self):
        if self.length == 0:
            sys.stdout.write('-1\n')
        else:
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next
            sys.stdout.write(str(iterator.item) + '\n')

def solution():
    n = int(sys.stdin.readline().rstrip())
    queue = LinkedQueue()

    for i in range(n):
        line = sys.stdin.readline().split()
        if line[0] == 'push':
            queue.push(line[1])
        elif line[0] == 'pop':
            queue.pop()
        elif line[0] == 'size':
            queue.size()
        elif line[0] == 'empty':
            queue.empty()
        elif line[0] == 'front':
            queue.front()
        elif line[0] == 'back':
            queue.back()

solution()