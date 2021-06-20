def solution(A, K):
    length = len(A)

    if not A or K == 0:
        return A

    K = K % length

    new_A = [0 for _ in range(length)]

    i = 0
    while i < length:
        new_A[K] = A[i]
        i += 1
        K = (K + 1) % length

    return new_A

A = [1,2,3,4,5,6,7,8]
K = -3
solution(A, K)


# a = [1,2,3,4,5]
#
# k = -3
#
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
#
# k = -3%len(a)
# print(k)

# a = [1,2,3,4,5,6,7,8]
# print(-3%len(a))
# 4 5 6 7 8 1 2 3
#
# 2 3 4 5 6 7 8 1
# 3 4 5 6 7 8 1 2
# 4 5 6 7 8 1 2 3