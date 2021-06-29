# baekjoon 11724 연결요소의 개수

import sys

def num_of_connection_elements(matrix, visit):
    result = 0

    # 모든 정점 순회
    for i in range(1, len(matrix)):
        # 이미 방문한 경우
        if visit[i] == 1:
            continue
        
        # 또 하나의 연결요소 발견
        result += 1
        # 스택에 시작 정점 넣고 시작
        stack = [i]

        # dfs
        while stack:
            cur = stack.pop()
            if visit[cur] == 1:
                continue

            visit[cur] = 1

            for j in range(1, len(matrix)):
                if not visit[j] and (matrix[cur][j] == 1 or matrix[j][cur] == 1) :
                    stack.append(j)

    print(result)

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
matrix = [[0 for i in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    matrix[x][y] = 1
num_of_connection_elements(matrix, visit)
