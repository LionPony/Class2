# 최소 힙
# https://www.acmicpc.net/problem/1927
import sys

class Node:
    def __init__(self, item=None):
        self.parent = None
        self.left = None
        self.right = None
        if item:
            self.item = item

class My_MinimumHeap:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, item):
        self.count += 1
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            return

        parent = self.head
        binaryNum = bin(self.count)[3:]
        for direction in binaryNum[:-1]:
            if direction == '0':
                parent = parent.left
            else:
                parent = parent.right
        if binaryNum[-1] == '0':
            parent.left = newNode
        else:
            parent.right = newNode
        newNode.parent = parent

        self._heap_Up(newNode)

    def _heap_Up(self, node):
        while node.parent is not None and node.item < node.parent.item:
            node.item, node.parent.item = node.parent.item, node.item
            node = node.parent

    def delete(self):
        if self.head is None:
            return '0'

        result = self.head.item

        if self.head.left is None and self.head.right is None:
            self.head = None
            self.count -= 1
            return result

        lastNode = self.head
        binaryNum = bin(self.count)[3:]
        for direction in binaryNum:
            if direction == '0':
                lastNode = lastNode.left
            else:
                lastNode = lastNode.right

        self.head.item = lastNode.item

        if lastNode.parent.left == lastNode:
            lastNode.parent.left = None
        else:
            lastNode.parent.right = None

        self._heap_Down(self.head)

        self.count -= 1
        return result

    def _heap_Down(self, node):
        while node.left:
            min_Child = node.left
            if node.right and node.right.item < node.left.item:
                min_Child = node.right

            if node.item > min_Child.item:
                node.item, min_Child.item = min_Child.item, node.item
                node = min_Child
            else:
                break

def solution():
    n = int(sys.stdin.readline().strip())
    my_Heap = My_MinimumHeap()
    for _ in range(n):
        command = int(sys.stdin.readline().rstrip())
        if command == 0:
            sys.stdout.write(my_Heap.delete() + '\n')
        else:
            my_Heap.insert(str(command))

solution()