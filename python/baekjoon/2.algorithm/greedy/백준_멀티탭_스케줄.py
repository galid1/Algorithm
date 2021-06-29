n, k = map(int, input().split())
s = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0
for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            try:
                if a < s[i + 1:].index(m[j]):
                    a = s[i + 1:].index(m[j])
                    b = j
            except:
                a = -1
                b = j
                break
        m[b] = s[i]
        cnt += 1
print(cnt)