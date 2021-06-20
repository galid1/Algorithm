def solution(A):
    A = set(A)

    num = 1
    while True:
        if num not in A:
            break

        num += 1

    return num


A = [2, 3, 1, 5]
solution(A)
