# 백준 1158 조세퍼스 문제

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def josephus(self, n, k):
        before = self.head
        start = self.head
        next_start = self.head
        result = []

        while len(result) < n:
            for j in range(k - 1):
                before = start
                start = start.next
            # 다음 시작위치 지정
            next_start = start.next
            # 삭제될 것 result에 담기
            result.append(start)
            # 삭제
            before.next = next_start
            # 시작위치 변경
            start = next_start

        print("<", end="")
        for i in range(len(result)):
            if i == len(result) - 1:
                print(result[i].data, end="")
                break
            print(result[i].data, end=", ")
        print(">")


n, k = list(map(int, sys.stdin.readline().rstrip().split(" ")))
ll = LinkedList()
for i in range(n):
    ll.add_last(i+1)
ll.josephus(n, k)

