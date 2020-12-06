from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dodam.settings")
import django
django.setup()
from dodamweb.models import *


def getBookInfoCrawler(url):
    # 본인의 크롬드라이버 경로 설정
    chromedriver = 'chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')
    driver = webdriver.Chrome(executable_path="/home/ubuntu/dodam_dodam/dodam/chromedriver", chrome_options=chrome_options)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/8);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight/8, document.body.scrollHeight/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight/4, document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight/1);")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    book_name = soup.find("a", {'class': 'Ere_bo_title'})
    writer = soup.find("a", {'class': 'Ere_sub2_title'})
    book_img = soup.find("img", {'class': 'imgbox'})
    introduce_book = driver.find_elements_by_class_name('Ere_prod_mconts_box')
    temp_book_info = book_info()
    for i in introduce_book:
        if '책소개' in i.text:
            if '출판사 제공 책소개' not in i.text:
                temp_book_info.short_intro = i.text

    temp_book_info.book_name = book_name.text
    temp_book_info.writer = writer.text
    temp_book_info.book_img = book_img['src']
    temp_book_info.url = url
    temp_book_info.save()
    result = []
    try:
        sample = driver.find_element_by_xpath('//*[@id="Underline3_more"]/a')
        sample.click()

    except:
        result.append('클릭못함')


    try:
        moreList = soup.find_all("span", {"id": re.compile('more')})
        for td in moreList:
            temp_in_book = in_book()
            temp_in_book.book_name = book_name.text
            temp_in_book.full_intro = td.get_text()
            temp_in_book.save()

    except:
        result.append("책속에서없음")

    driver.close()
    return



