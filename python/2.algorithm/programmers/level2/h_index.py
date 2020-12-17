def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    flag = False
    for i in range(len(citations)):
        if citations[i] < i+1:
            answer = i
            flag = True
            break

    if not flag:
        answer = len(citations)

    return answer
 
solution([0])
solution([2, 2])
solution([4, 4, 4, 4])
solution([3, 0, 6, 1, 5])
