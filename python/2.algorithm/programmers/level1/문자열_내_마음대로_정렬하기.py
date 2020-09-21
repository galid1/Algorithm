def solution(strings, n):
    strings = sorted(strings)

    # a < b < c
    sort_str(strings, n)

    return strings

def sort_str(arr, n):
    for i in range(len(arr), 0, -1):
        for j in range(0, i-1):
            if arr[j][n] > arr[j+1][n]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



