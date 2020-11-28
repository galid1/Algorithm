class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = 101
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos


    def rightChild(self, pos):

        return (2 * pos) + 1

    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))


    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


def solution():
    votes = [5, 10, 7, 3, 8]

    maxHeap = MaxHeap(51)
    for i in range(1, len(votes)):
        maxHeap.insert(votes[i])

    answer = 0
    while votes[0] < maxHeap.Heap[1]:
        print(maxHeap.Heap[1])
        votes[0] += 1
        answer += 1
        maxHeap.insert(maxHeap.extractMax() - 1)

    return answer

print(solution())