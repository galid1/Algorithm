def dailyTemperatures(temperatures):
    day_len = len(temperatures)
    ans = [0 for _ in range(day_len)]

    stack = []

    for i in range(day_len - 1, -1, -1):
        need_day = 1
        cur_temp = temperatures[i]

        while stack and cur_temp >= stack[-1][0]:
            need_day += stack.pop()[1]

        if not stack:
            stack.append((cur_temp, 0))
            ans[i] = 0
        else:
            stack.append((cur_temp, need_day))
            ans[i] = need_day

    return ans


# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(dailyTemperatures(temperatures))
