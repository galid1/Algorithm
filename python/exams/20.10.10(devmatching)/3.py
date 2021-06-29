def solution(n, groups):
    answer = 0

    # 켤수 있는 크기 순으로 정렬
    groups.sort(key=lambda item : item[1] - item[0], reverse=True)

    v = [0 for i in range(0, n+1)]

    for g in groups:
        cnt = 0
        for j in range(g[0], g[1]+1):
            if not v[j]:
                cnt += 1

        # 그룹을 사용하기로 결정
        if cnt >= 1:
            answer += 1

        for j in range(g[0], g[1]+1):
            v[j] = 1

    # 하나씩 켜는경우를 센다
    for k in range(1, len(v)):
        if not v[k]:
            answer += 1


    return answer




solution(10, [[1, 5], [2, 7], [4, 8], [3, 6]])
# solution(7, [[6, 7],[1, 4],[2, 4]])
# solution(100, [[1, 50],[1,100],[51, 100 ]])