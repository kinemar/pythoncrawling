## 라이브러리 호출
### DB라이브러리는 직접 db.py file로 먼저 생성 후 테스트

import mechanicalsoup
import pandas as pd

browser = mechanicalsoup.StatefulBrowser()
browserurl = "https://www.google.com/search?q="

search_target = input("키워드를 입력하세요 : ")
browserurl = browserurl + search_target
browserurl = browserurl.replace(" ", "+")
browser.open(browserurl)

## 브라우저 런치 필요시 아래 주석 표시 삭제
# browser.launch_browser()

th = browser.page.findAll("div",{"class":"BNeawe vvjwJb AP7Wnd"})
linkth = browser.page.findAll("div",{"class":"egMi0 kCrYT"})
## 포스트 이름
distribution = [value.text for value in th]
search_DF = pd.DataFrame(distribution,columns=["name"])

## 포스트 링크
link_data = list()

## 링크 제작
try :
    i = 0
    while i < len(linkth):
        link_data.append(linkth[i].find("a").attrs["href"].split("q=")[1])
        i += 1
    search_DF['link'] = link_data
except :
    print("관련된 링크가 없습니다.")
