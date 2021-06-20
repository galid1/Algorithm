def solution(X, Y, D):
    t = Y-X

    if t%D == 0:
        return t//D
    else:
        return t//D + 1


X = 101
Y = 888
D = 30

print(solution(X,Y,D))