import sys


def solution(i, j):
    global papers_count, paper, min_count

    # 정답
    if i >= len(paper[0]):
        result = 0
        for ci in range(1, len(papers_count)):
            result += 5 - papers_count[ci]
        min_count = min(min_count, result)
        return

    if paper[i][j] == 1:
        # 5*5부터 덮을 수 있는지 확인하고 덮음
        for k in range(5, 0, -1):
            if has_more_paper(k) and can_cover(i, j, k):
                cover(i, j, k)
                if j < len(paper) - 1:
                    solution(i, j+1)
                elif i < len(paper):
                    solution(i+1, 0)
                uncover(i, j, k)

    else:
        if j < len(paper[0]) - 1:
            solution(i, j+1)
        elif i < len(paper):
            solution(i+1, 0)


def has_more_paper(paper_size):
    global papers_count
    if papers_count[paper_size] == 0:
        return False
    else:
        return True


def can_cover(start_i, start_j, paper_size):
    global paper, papers_count

    if (start_i + paper_size - 1) >= len(paper) or (start_j + paper_size - 1) >= len(paper):
        return False

    if papers_count[paper_size] <= 0:
        return False

    for i in range(start_i, start_i + paper_size):
        for j in range(start_j, start_j + paper_size):
            if paper[i][j] != 1:
                return False

    return True


def cover(start_i, start_j, paper_size):
    global paper, papers_count

    papers_count[paper_size] -= 1

    for i in range(start_i, start_i + paper_size):
        for j in range(start_j, start_j + paper_size):
            paper[i][j] = 0


def uncover(start_i, start_j, paper_size):
    global paper, papers_count

    papers_count[paper_size] += 1

    for i in range(start_i, start_i + paper_size):
        for j in range(start_j, start_j + paper_size):
            paper[i][j] = 1


# 1*1 -> 5*5
papers_count = [5 for _ in range(6)]
paper = []
for i in range(10):
    paper.append(list(map(int, sys.stdin.readline().strip().split(" "))))

min_count = 101
solution(0, 0)

# 정답 출력
if min_count == 101:
    print(-1)
else:
    print(min_count)
