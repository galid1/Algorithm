from urllib.error import HTTPError
from selenium import webdriver
from openpyxl import Workbook,load_workbook
import datetime


##파일 열고 닫는 위치를 조정해야할 듯


# 날짜
now = datetime.datetime.now()
date = now.strftime('%Y.%m.%d')
# Product_list 파일 위치
product_file_path = 'C:/test/'
# Product_list 파일 이름
product_file_name = 'product.txt'
# Excel 파일 저장 위치
excel_file_path = 'C:/test/'
# Excel 파일 이름
excel_file_name = excel_file_path + date + '.xlsx'
# Excel sheet 이름
excel_sheet_title = 'confirm'
# Excel 행
excel_row = 2

## Excel파일 생성 메소드
def make_excel():
    work_book = Workbook()
    sheet1 = work_book.active
    sheet1.title = excel_sheet_title

    #헤더 입력
    sheet1.cell(row=1, column=1).value = '상품ID'
    sheet1.cell(row=1, column=2).value = '규격'
    sheet1.cell(row=1, column=3).value = 'Title'
    sheet1.cell(row=1, column=4).value = 'Description'
    sheet1.cell(row=1, column=5).value = 'CAS Number'
    sheet1.cell(row=1, column=6).value = '확인가능'
    sheet1.cell(row=1, column=7).value = '가격'
    sheet1.cell(row=1, column=8).value = 'Storage Temp'
    sheet1.cell(row=1, column=9).value = '비고'

    work_book.save(filename=excel_file_name)
    work_book.close()


## Product_list 로딩 메소드
# def get_products_from_file():
#     product_file = open(product_file_path + "/product.txt", 'r')
#     product_list = []
#
#     lines = product_file.readlines()
#     for line in lines:
#         product_list.append(line)
#     product_file.close()
#
#     return product_list


## 크롤링을 위한 메소드
def make_request():
    product_file = open(product_file_path + product_file_name, 'r')

    for product_code in product_file.readlines():
        try:
            url = 'https://www.sigmaaldrich.com/catalog/search?term=' + product_code
            driver = webdriver.Chrome('/Users/galid/chrome_driver/chromedriver')
            driver.get(url)

            search_result = driver.find_element_by_xpath(
                "//*[@id='searchResultContainer-inner']/div[7]/div/div[2]/div[2]/div[1]/ul/li[2]/a")

            search_result.click()
            parsing_data(driver)

        except HTTPError as e:
            pass

        global excel_row
        excel_row += 1

    product_file.close()


## 크롤링한 데이터로부터 원하는 정보를 파싱하는 메소드
def parsing_data(driver):
    crawling_results = []

    #H1, H2 데이터 불러오기
    crawling_results.append(driver.find_element_by_xpath('//*[@id="productDetailHero"]/div/div[1]/h1').text) #title
    crawling_results.append(driver.find_element_by_xpath('//*[@id="productDetailHero"]/div/div[1]/h2[2]').text) #description

    #Table안의 데이터 불러오기
    tr = driver.find_element_by_xpath('// *[ @ id = "pricingContainerMessage"] / div / div / table / tbody / tr[2]')

    try : #td 내용 존재하는 경우(sku, shipping, price)
        tds = tr.find_elements_by_tag_name('td')
        crawling_results.append(tds[0].text) #sku
        crawling_results.append(tds[1].text) #shipping
        crawling_results.append(tds[3].text) #price
    except : #내용 존재하지 않는 경우(비고)
        note = 'To order products, please contact your local dealer.'

    insert_data_to_excel(crawling_results)


def insert_data_to_excel(crawling_results):
    excel_file = load_workbook(excel_file_name)
    sheet1 = excel_file[excel_sheet_title]

    excel_column = 3
    for data in crawling_results:
        sheet1.cell(row=excel_row, column=excel_column).value = data
        excel_column += 1

    excel_file.save(excel_file_name)
    excel_file.close()


make_excel()
make_request()