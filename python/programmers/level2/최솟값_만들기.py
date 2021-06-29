def solution(a, b):
    answer = 0

    a.sort()
    b.sort()

    for i in range(len(a)):
        answer += a[i]  * b[len(a)-i-1]

    return answer

solution([1,4,2], [5,4,4])
solution([1,2], [3,4])