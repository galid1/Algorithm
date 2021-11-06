def solution(grid, clockwise):
    answer = []
    n = len(grid)

    if clockwise:
        for stair in range(n - 1, -1, -1):
            s = ''
            idx = 0

            for i in range(n - stair):
                while idx <= i*2:
                    s += grid[stair+i][idx]
                    idx += 1
            answer.append(s[-1::-1])

    else:
        for stair in range(n-1, -1, -1):
            s = ''
            idx = -1

            for i in range(n - stair):
                while idx >= i * -2 - 1:
                    s += grid[stair+i][idx]
                    idx -= 1
            answer.append(s)

    return answer


grid = ["1","234","56789"]
clockwise = True
# grid = ["1", "234", "56789", "1234567"]

grid = ["A","MAN","DRINK","WATER11"]
clockwise = False
print(solution(grid, clockwise))
