import sys

def solution(n):
    n = 1000 - n
    answer = 0

    answer += n//500
    n %= 500

    answer += n//100
    n %= 100

    answer += n//50
    n %= 50

    answer += n//10
    n %= 10

    answer += n//5
    n %= 5

    answer += n//1
    n %= 1

    print(answer)


n = int(sys.stdin.readline())
solution(n)