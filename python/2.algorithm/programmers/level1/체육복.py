def solution(n, lost, reverse):
    answer = 0

    # 최초 체육복개수 1로
    children = [1 for i in range(n)]

    # 도난 당한 친구들의 옷을 1씩 줄임
    for l in lost:
        children[l-1] -= 1

    # 여벌옷 있는 친구들의 옷을 1씩 늘림
    for r in reverse:
        children[r-1] += 1

    for ci in range(0, len(children)):
        # 여벌옷 있는 경우
        if children[ci] == 2:
            # 앞 친구가 도난 당한 경우
            before_idx = ci - 1
            if before_idx >= 0 and children[before_idx] == 0:
                children[ci] -= 1
                children[ci - 1] += 1
                # 이미 앞친구를 빌려준경우 뒷친구를 빌려줄수 없음
                continue
            # 뒷 친구가 도난 당한 경우
            next_idx = ci + 1
            if next_idx < len(children) and children[next_idx] == 0 :
                children[ci] -= 1
                children[ci + 1] += 1

    # 체육복이 있는 학생수
    for c in children:
        if c != 0:
            answer += 1

    return answer


print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
