import sys


def solve(words):
    ans = 0
    for word in words:
        visited = {chr(i): False for i in range(ord('a'), ord('z')+1)}

        is_group_word = True
        idx = 0
        while True:
            # 이미 나왔던 문자가 띄워서 나온다면 그만
            c = word[idx]

            if visited[c]:
                is_group_word = False
                break

            visited[c] = True
            idx += 1
            while idx < len(word) and word[idx] == c:
                idx += 1

            if idx == len(word):
                break

        # 그룹단어라면 정답 1증가
        if is_group_word:
            ans += 1

    print(ans)


n = int(sys.stdin.readline().strip())
words = []
for _ in range(n):
    words.append(list(sys.stdin.readline().strip()))
solve(words)