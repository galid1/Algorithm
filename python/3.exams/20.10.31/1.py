def solution(n, delivery):
    # 배송여부 1기준 정렬
    delivery.sort(key= lambda d : d[2], reverse = True)

    # 재고량
    sup = [0 for i in range(n+1)]

    # 존재하는 재고 표시
    idx = 0
    for d in delivery:
        if d[2] == 0:
            break
        sup[d[0]] = 1
        sup[d[1]] = 1
        idx += 1

    for i in range(idx, len(delivery)):
        d = delivery[i]
        if sup[d[0]] == 1:
            sup[d[1]] = -1
        elif sup[d[1]] == 1:
            sup[d[0]] = -1

    answer = ''
    for j in range(1, len(sup)):
        if sup[j] == 0:
            answer += '?'
        elif sup[j] == 1:
            answer += 'O'
        elif sup[j] == -1:
            answer += 'X'

    return answer


delivery = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]
print(solution(6, delivery))