import sys
#n번째 피보나치 수를 구하는 알고리즘

#Top-down
memo = [0 for i in range (100)]
def fibonacci_top_down(n):
    if memo[n] > 0:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return memo[n]

    else:
        memo[n] = fibonacci_top_down(n-1) + fibonacci_top_down(n-2)
        return memo[n]

#Bottom-up
def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    fir = 0
    sec = 1
    for i in range(0, n-1):
        next = fir+sec
        fir = sec
        sec = next
    return next


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    #print(fibonacci_top_down(n))
    print(fibonacci_bottom_up(n))