graph = {
    '1': ['2', '3'],
    '2': ['1', '4'],
    '3': ['1', '4', '5'],
    '4': ['2', '3'],
    '5': ['3']
}

def bfs(start):
    queue = [start]
    visit = [start]

    while queue:
        cur = queue.pop(0)
        print(cur)

        for link in graph[cur]:
            if link not in visit:
                visit.append(link)
                queue.append(link)

bfs('1')