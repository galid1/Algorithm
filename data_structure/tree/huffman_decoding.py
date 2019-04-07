#hackerrank huffman decoding

# 문자는 빈도에 따라서 이진수로 맵핑됨
# 문자가 자주 반복될 수록 짧은 이진수에 맵핑됨
# 이진 트리를 이용하여 각 문자를 이진수로 맵핑함 왼쪽은 0 우측은 1
# 각 서브트리의 루트 노드는 양 자식노드의 합을 값으로 가짐

import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


def decodeHuff(root, s):
    arr = list(map(int,s))
    result = []

    cur = root
    for i in arr:
        if i == 0 and cur.left:
            cur = cur.left
            if not cur.left and not cur.right:
                result.append(cur.data)
                cur = root
        if i == 1 and cur.right:
            cur = cur.right
            if not cur.left and not cur.right:
                result.append(cur.data)
                cur = root
    for i in result:
        print(i, end='')


ip = input()
freq = {}

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()

code_hidden = {}

dfs_hidden(root, "")

if len(code_hidden) == 1:
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
