from collections import deque


graph = {
    '1': ['2', '3'],
    '2': ['1', '4'],
    '3': ['1', '4', '5'],
    '4': ['2', '3'],
    '5': ['3']
}

def bfs():
    global graph

    v = []
    q = deque(['1'])
    v.append('1')

    while q:
        cur = q.popleft()
        print(cur)

        for link in graph[cur]:
            if link not in v:
                v.append(link)
                q.append(link)

bfs()
