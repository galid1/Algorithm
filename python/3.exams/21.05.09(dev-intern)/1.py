def solution(code, day, data):
    answer = []

    data = split_data(data)

    for hh, price in data[code][day]:
        answer.append(int(price))

    return answer


# code, day 이중 사전형 자료 반환
def split_data(data):
    splitted_data = {}

    for d in data:
        ds = d.split(" ")
        price = ds[0].split("=")[1]
        code = ds[1].split("=")[1]
        time = ds[2].split("=")[1]
        ymd, hh = time[:8], time[8:]

        if code not in splitted_data.keys():
            # { code : {day : } }
            splitted_data[code] = {ymd: [(hh, price)]}

        else:
            if ymd not in splitted_data[code].keys():
                splitted_data[code][ymd] = [(hh, price)]
            else:
                splitted_data[code][ymd].append((hh, price))

    for c in splitted_data.keys():
        for key in splitted_data[c].keys():
            splitted_data[c][key].sort()

    return splitted_data


code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
solution(code, day, data)