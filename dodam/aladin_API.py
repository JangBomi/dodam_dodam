import os
import sys
import requests
import json


def search_url(title):
    title= title
    #url 정의 및 reqeust와 response
    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbpearlisrich1647001&Query={title}&QueryType=Keyword&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101"

    response = requests.get(url)

    #데이터 json으로 변환
    response_json = json.loads(response.text)

    #check
    print(response_json)


    item_list = response_json['item']
    temp_url = item_list[0]['link']




    return temp_url
