def solve(A):
    paring = set()

    for num in A:
        if num not in paring:
            paring.add(num)
        else:
            paring.remove(num)

    return paring.pop()


A = [9, 3, 9, 3, 9, 7, 9]
solve(A)