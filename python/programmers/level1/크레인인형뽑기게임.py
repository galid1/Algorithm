# 프로그래머스 Level 1 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0

    stack = []

    for move in moves:
        for ri in range(len(board)):
            target = board[ri][move - 1]

            # 인형이 존재
            if target != 0:
                # 인형을 들어서
                board[ri][move - 1] = 0
                # 스택에 넣음
                stack.append(target)

                # 같은 인형이 두개가 겹치면 터뜨리기
                answer += crush(stack)
                break

    return answer


# 같은 인형 터뜨린 개수 반환
def crush(stack):
    count = 0

    while True:
        if len(stack) < 2:
            break

        if stack[-1] != stack[-2]:
            break

        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count += 2

    return count



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

