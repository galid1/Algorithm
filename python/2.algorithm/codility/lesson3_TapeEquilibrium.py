def solution(A):
    fir_sum = A[0]
    sec_sum = sum(A[1:])

    min_sub = (abs(fir_sum - sec_sum))
    for i in range(1, len(A)-1):
        fir_sum += A[i]
        sec_sum -= A[i]

        min_sub = min(min_sub, abs(fir_sum - sec_sum))

    return min_sub

A = [3, 1, 2, 4, 3]
solution(A)
