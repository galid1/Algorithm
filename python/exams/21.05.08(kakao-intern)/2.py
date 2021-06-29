from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(places):
    answer = []

    for place in places:
        splitted_place = split_place(place)
        answer.append(check(splitted_place))

    return answer


# 각 칸을 나누어 배열로 만듦
def split_place(place):
    splitted_place = []

    for p in place:
        splitted_place.append(list(p))

    return splitted_place


# 각 place가 거리두기를 지키는지 확인
def check(place):
    applicants = find_applicant(place)

    # 지원자가 없는 경우 거리두기 OK
    if not applicants:
        return 1

    # 각 지원자 별 dfs
    for p in applicants:
        q = deque([(p[0], p[1], 0)])
        visited = [[False for _ in range(len(place[0]))] for _ in range(len(place))]
        visited[p[0]][p[1]] = True
        while q:
            for _ in range(len(q)):
                cx, cy, distance = q.popleft()

                for dx, dy in ds:
                    nx, ny, nd = cx+dx, cy+dy, distance+1

                    if nd > 2:
                        continue

                    if 0 <= nx < len(place) and 0 <= ny < len(place[0]) and not visited[nx][ny]:
                        # 지원자가 맨해튼 거리 2이내
                        if place[nx][ny] == 'P':
                            return 0

                        if place[nx][ny] == 'O':
                            q.append((nx, ny, nd))
                            visited[nx][ny] = True

    # 모든 지원자가 거리두기 지킴
    return 1



# 각 place의 지원자 위치 배열을 반환
def find_applicant(place):
    applicants = []
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == 'P':
                applicants.append((i, j))

    return applicants



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)