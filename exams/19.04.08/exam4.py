import sys
import queue
import requests

def  getMovieTitles(substr):
    # 기본 url 설정
    base_url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='
    base_url += substr + '&page='

    # 응답 받고 json으로 만들기
    response = requests.get(base_url+str(1))
    page_json = response.json()
    page_num = page_json['total_pages']

    # result
    result = []

    for i in range(1, page_num + 1):
        response = requests.get(base_url + str(i))
        response_json = response.json()
        for j in range(0, len(response_json['data'])):
            result.append(response_json['data'][j]['Title'])

    result.sort()
    return result

print(getMovieTitles('spiderman'))





