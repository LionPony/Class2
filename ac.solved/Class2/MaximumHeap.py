# 최대 힙
# https://www.acmicpc.net/problem/11279
import sys

class My_MaximumHeap:
    def __init__(self):
        self.heap_Array = []

    def add(self, item):
        self.heap_Array.append(item)
        self._heap_Up(len(self.heap_Array) - 1)

    def _heap_Up(self, index):
        parent = (index-1)//2
        while index > 0 and self.heap_Array[parent] < self.heap_Array[index]:
            self.heap_Array[parent], self.heap_Array[index] = self.heap_Array[index], self.heap_Array[parent]
            index = parent
            parent = (index-1)//2

    def delete(self):
        if len(self.heap_Array) == 0:
            return 0
        if len(self.heap_Array) == 1:
            return self.heap_Array.pop()
        self.heap_Array[0], self.heap_Array[-1] = self.heap_Array[-1], self.heap_Array[0]
        result = self.heap_Array.pop()
        self._heap_Down()
        return result

    def _heap_Down(self, index=0):
        count = len(self.heap_Array)
        while True:
            left = 2*index+1
            right = 2*index+2
            largest = index
            if left < len(self.heap_Array) and self.heap_Array[left] > self.heap_Array[largest]:
                largest = left
            if right < len(self.heap_Array) and self.heap_Array[right] > self.heap_Array[largest]:
                largest = right
            if largest == index:
                return

            self.heap_Array[index], self.heap_Array[largest] = self.heap_Array[largest], self.heap_Array[index]
            index = largest

def solution():
    n = int(sys.stdin.readline().rstrip())
    my_MaximumHeap = My_MaximumHeap()
    for _ in range(n):
        command = int(sys.stdin.readline().rstrip())
        if command == 0:
            sys.stdout.write(str(my_MaximumHeap.delete()) + '\n')
        else:
            my_MaximumHeap.add(command)

solution()