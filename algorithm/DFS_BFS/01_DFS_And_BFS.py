class Queue:
    queue = []
    front = 0
    rear = 0
    size = 0

    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.size = 0
        self.queue = [0 for i in range(0, size)]

    def is_empty(self):
        if self.front == self.rear :
            return True
        return False

    def is_full(self):
        if (self.rear + 1)%len(self.queue) == self.front :
            return True
        return False

    def enqueue(self, item):
        if self.is_full() is False :
            self.rear = (self.rear + 1)%len(self.queue)
            self.queue[self.rear] = item
            self.size += 1

    def dequeue(self):
        if self.is_empty() is False :
            self.front = (self.front + 1)%len(self.queue)
            item = self.queue[self.front]
            self.queue[self.front] = 0
            self.size -= 1
            return item

    def print_queue(self):
        print(self.queue)

class Node:
    node_num = -1
    links = []
    is_visited = -1

    def __init__(self, node_num):
        self.node_num = node_num
        self.links = [None]
        self.is_visited = -1

    def link(self, node):
        self.links.append(node)
        self.sort()

    def sort(self):
        for i in range(1, len(self.links) - 1):
            min = i
            for j in range(i + 1, len(self.links)):
                if self.links[min].node_num > self.links[j].node_num:
                    min = j
            temp = self.links[i]
            self.links[i] = self.links[min]
            self.links[min] = temp

class Graph:
    node_count = -1
    start_node = -1
    nodes = [0]

    def __init__(self, init_infos):
        self.node_count = int(init_infos[0])
        self.start_node = int(init_infos[2])
        self.make_nodes()

    def make_nodes(self):
        for i in range(1, self.node_count+1 , 1) :
            node = Node(i)
            self.nodes.insert(i, node)

    def make_link(self, node_nums):
        self.nodes[int(node_nums[0])].link(self.nodes[int(node_nums[1])])
        self.nodes[int(node_nums[1])].link(self.nodes[int(node_nums[0])])

    def visit_clear(self):
        for i in range(1, len(self.nodes)):
            self.nodes[i].is_visited = False

    def dfs(self, node):
        print(node.node_num, end=" ")
        node.is_visited = True
        for i in range(1, len(node.links)):
            if node.links[i].is_visited == -1:
                self.dfs(node.links[i])

    def bfs(self):
        queue = Queue(self.node_count)
        queue.enqueue(self.nodes[self.start_node])

        while not queue.is_empty() :
            node = queue.dequeue()
            node.is_visited = True
            print(node.node_num, end=" ")

            for j in range(1, len(node.links)):
                if node.links[j].is_visited is False:
                    queue.enqueue(node.links[j])
                    node.links[j].is_visited = True


graph_init_infos = str(input()).split(" ")
graph = Graph(graph_init_infos)

for i in range(0,int(graph_init_infos[1]),1):
    link_infos = str(input()).split(" ")
    graph.make_link(link_infos)

graph.dfs(graph.nodes[graph.start_node])
graph.visit_clear()
print()
graph.bfs()