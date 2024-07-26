## 라이브러리 호출
### DB라이브러리는 직접 db.py file로 먼저 생성 후 테스트
import mechanicalsoup
import pandas as pd
import db

browser = mechanicalsoup.StatefulBrowser()
browserurl = "https://namu.wiki/w"

i = '1'
while(1):
    i = input("Enter keywords: ")
    if i == '0':
        break
    keywords = "/" + i
    browserurl = browserurl + keywords


browser.open(browserurl)
## 페이지 확인시에 사용하는 브라우저 호출
## browser.launch_browser()

## 데이터 뽑아오기 (나무위키 보드게임 종류 확인)
th = browser.page.findAll("a",{"class": "wiki-link-internal"})
i = 0
distribution = [value.text.replace("(보드 게임)","").replace("(보드게임)","") for value in th]

## 데이터 관련 링크 뽑아오기
href_b = th[0].attrs["href"]
dfh = pd.DataFrame()
dfh['Nhr'] = th[0].attrs['href']
while(i<len(th)):
    href_b = th[i].attrs["href"]
    href_b = 'namu.wiki' + href_b
    dfh.loc[i] = [href_b]
    i+=1
board_game_list = pd.DataFrame(distribution)

board_game_list['href'] = dfh['Nhr']
board_game_list1 = board_game_list.iloc[77:]
board_game_list1 = board_game_list1.rename(columns={0:'name'})
board_game_list1.index = board_game_list1['name']
distribution = distribution[77:]
print(board_game_list1)

## MongoDB
try:
    db.collection.insert_many(board_game_list1.to_dict('records'))
    print("Data Save Successfully!!")

except Exception as e:
    print("Save Failed...")