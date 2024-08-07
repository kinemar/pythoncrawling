## 라이브러리 호출

import mechanicalsoup
import pandas as pd

browser = mechanicalsoup.StatefulBrowser()
browserurl = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

search_target = input("키워드를 입력하세요 : ")
browserurl = browserurl + search_target
browserurl = browserurl.replace(" ", "+")


search_num = 0
## 브라우저 런치 필요시 아래 주석 표시 삭제
# browser.launch_browser()
browser.open(browserurl)
th = browser.page.findAll("a",{"class": "title_link"})

## 포스트 이름
distribution = [value.text for value in th]
search_DF = pd.DataFrame(distribution,columns=["name"])

## 포스트 링크
link_data = list()

## 링크 제작
try :
    i = 0
    while i < len(th):
        link_data.append(th[i].attrs['href'])
        i += 1
    search_DF['link'] = link_data
except :
    print("문제가 발생하였습니다.")