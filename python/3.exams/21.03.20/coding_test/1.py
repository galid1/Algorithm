def solution(table, languages, preference):
    job_table = {0: "SI", 1: "CONTENTS", 2: "HARDWARE", 3: "PORTAL", 4: "GAME"}
    lan_pre = {languages[i]:preference[i] for i in range(len(languages))}

    # ans table
    ans = {"SI": 0, "CONTENTS": 0, "HARDWARE": 0, "PORTAL": 0, "GAME": 0}

    # make score_table
    score_table = {}
    for i in range(len(table)):
        temp = list(table[i].split(" "))
        scores = temp[1:]
        scores.reverse()
        job = temp[0]
        score_table[job] = [''] + scores

    # 각 직업군 순회하며 점수 계산
    for job in score_table.keys():
        sums = 0
        for lan in languages:
            job_score = score_table[job].index(lan) if lan in score_table[job] else 0
            sums += job_score * lan_pre[lan]

        ans[job] = sums

    ans = dict(sorted(ans.items(), key=lambda items: items[0]))
    ans = sorted(ans.items(), key=lambda items: items[1], reverse=True)

    return ans[0][0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
solution(table, languages, preference)