from config  import *
import requests
import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET



result = []

page = 1
type = 1

def get_request_url(page):
    url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
    parameter = '?serviceKey=' + serviceKey
    parameter += '&pageNo=' + str(page)
    parameter += '&numOfRows=10'
    # parameter += 'spclAdmTyCd=97'
    url = url + parameter

    res = requests.get(url)
    if res.status_code == 200:
        # print('접속성공했습니다 testCOVID_C.py문서 데이터 조작및 추출작업이 가능합니다 \n')
        ret = res.text
        # print('ret결과\n', ret)
    else:
        print(url, ' 접속실패')
    return ret



def make_file(result):

    csvSave = pd.DataFrame(result,columns=['pageNo','resultCode','resultMsg','numOfRows',
                                    'totalCount','adtFrDd','sgguNm','sidoNm','spclAdmTyCd',
                                    'telno','yadmNm'])
    csvSave.to_csv("./doc/COVID_hospital.csv", encoding="UTF-8", mode="w", index=False)
    print('-' * 50)
    print("./doc/COVID_hospital.csv file SAVE DONE!!!")



def main():
    for pageNum in range(1,12):

        data = get_request_url(pageNum)

        root = ET.fromstring(data)
        header = root.find('header')
        resultCode = header.find('resultCode').text
        resultMsg = header.find('resultMsg').text

        body = root.find('body')
        numOfRows = body.find('numOfRows').text
        pageNo = body.find('pageNo').text
        totalCount = body.find('totalCount').text
        items = body.find('items')


        for item in items:
            adtFrDd= item.find('adtFrDd').text
            sgguNm=item.find('sgguNm').text
            sidoNm=item.find('sidoNm').text
            spclAdmTyCd=item.find('spclAdmTyCd').text
            telno=item.find('telno').text
            yadmNm=item.find('yadmNm').text
            msg = [pageNo]+[resultCode]+[resultMsg]+[numOfRows]+[totalCount]+[adtFrDd]+[sgguNm]+[sidoNm]+[spclAdmTyCd]+[telno]+[yadmNm]
            #print(pageNo, sgguNm,  sidoNm, spclAdmTyCd, telno, '  kim')
            result.append(msg)

        print(result)
    print()
    make_file(result)

if __name__ == '__main__':
    main()
