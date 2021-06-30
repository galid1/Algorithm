def reorderLogFiles(logs):
    str_arrs, num_arrs = [], []

    for log in logs:
        split_log = log.split(" ")

        if split_log[1].isalpha():
            str_arrs.append([split_log[0]] + [' '.join(split_log[1:])] + [log])
        else:
            num_arrs.append(log)

    str_arrs.sort(key=lambda item: item[0])
    str_arrs.sort(key=lambda item: item[1])
    str_arrs = [item for id, data, item in str_arrs]

    return str_arrs + num_arrs


# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["j mo a", "5 moa", "g 07", "o 2 0", "t q h"]
print(reorderLogFiles(logs))
