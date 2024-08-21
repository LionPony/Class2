# 집합
# https://www.acmicpc.net/problem/11723
import sys

class My_Set:
    def __init__(self):
        self.s = set()

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        self.s.discard(x)

    def check(self, x):
        if x in self.s:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
            
    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = set(range(1,21))

    def empty(self):
        self.s.clear()

def solution():
    m = int(sys.stdin.readline().rstrip())
    s = My_Set()

    for i in range(m):
        command = sys.stdin.readline().split()
        cmd_type = command[0]

        if cmd_type == 'all':
            s.all()
        elif cmd_type == 'empty':
            s.empty()
        elif cmd_type == 'check':
            s.check(int(command[1]))
        elif cmd_type == 'toggle':
            s.toggle(int(command[1]))
        elif cmd_type == 'add':
            s.add(int(command[1]))
        elif cmd_type == 'remove':
            s.remove(int(command[1]))

solution()