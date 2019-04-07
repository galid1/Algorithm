import sys
class Heap:
    heap = []
    count = 0
    size = 0

    def __init__(self, size):
        self.heap = [-1 for i in range(0, size)]
        self.count = 0
        self.size = size

    #20씩 크기 증가
    def resizing(self):
        new_heap = [-1 for i in range(0, self.size + 20)]
        for i in range(0, self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap
        self.size = self.size + 20

    def is_empty(self):
        if self.count is 0:
            return True
        return False

    def is_full(self):
        if self.count is self.size-1:
            return True
        return False

    def insert_node(self, key):
        # if self.is_full():
        #     self.resizing()

        self.count += 1
        current_index = self.count

        while int(current_index/2) >= 1:
            if key <= self.heap[int(current_index/2)]:
                break
            self.heap[current_index] = self.heap[int(current_index/2)]
            current_index = int(current_index/2)
        self.heap[current_index] = key

    def delete_node(self):
        # 힙이 비었다면 0을 리턴
        if self.is_empty():
            return 0

        # 삭제될 원소의 값 기억
        delete_node = self.heap[1]
        # 마지막 원소를 루트로
        temp_node = self.heap[self.count]
        self.heap[1] = temp_node
        # 마지막 원소 삭제 처리
        self.heap[self.count] = -1
        # 노드 개수를 1 줄임
        self.count -= 1

        if self.count is 0:
            return delete_node

        current_node = 1
        child_node = current_node * 2 #왼쪽 자식 노드 (오른쪽 자식 노드 : 왼쪽 자식 노드 + 1)
        # 왼쪽노드가 전체 수보다 작으면 아직 비교대상이 존재한다는 것
        while child_node <= self.count:
            # 양쪽노드 존재(양쪽노드가 존재하지 않는다면 그냥 왼쪽 자식노드와 비교하면됨 따라서 else가 필요 없음)
            if child_node + 1 <= self.count:
                # 오른쪽 자식 노드가 더 크다면 그것을 비교 대상으로
                if self.heap[child_node] <= self.heap[child_node+1]:
                    child_node = child_node + 1
            # 루트에 놓인 마지막노드와 그 자식노드를 비교해가며 위치 조정
            if temp_node >= self.heap[child_node]:
                break

            self.heap[current_node] = self.heap[child_node]
            current_node = child_node
            child_node = child_node * 2

        self.heap[current_node] = temp_node
        return delete_node


if __name__ == "__main__":
    compute_count = int(sys.stdin.readline())
    heap = Heap(100000)
    for i in range(0, compute_count):
        compute = int(sys.stdin.readline())
        if compute is 0:
            print(heap.delete_node())
        else:
            heap.insert_node(compute)