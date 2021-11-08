import sys


def solve(start_idx, c):
    global s, visited, ans, max_n

    # 종료 조건
    if start_idx >= len(s):
        return True

    single_digit = int(s[start_idx])
    if not visited[single_digit]:
        visited[single_digit] = True
        ans.append(single_digit)
        if solve(start_idx+1, single_digit):
            return True
        visited[single_digit] = False
        ans.pop()

    if start_idx + 2 <= len(s):
        double_digit = int(s[start_idx:start_idx+2])
        if double_digit <= max_n and not visited[double_digit]:
            visited[double_digit] = True
            ans.append(double_digit)
            if solve(start_idx+2, double_digit):
                return True
            visited[double_digit] = False
            ans.pop()

    return False


def valid(num):
    global max_n

    return num <= max_n


s = sys.stdin.readline().strip()
visited = [False for _ in range(51)]
ans = []
max_n = len(s) if len(s) < 10 else 9 + (len(s)-9)//2
solve(0, 0)

for a in ans:
    print(a, end=' ')


# 11121231341451561678910

# 1112131410987654321