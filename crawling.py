## 라이브러리 호출
### DB라이브러리는 직접 db.py file로 먼저 생성 후 테스트
import mechanicalsoup


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
browser.page.find("div",{"class":"_4ofCJ8Ig"})
th = browser.page.findAll("a",{"class": "IuxDkZ2v"})
print(th)
i = 0
distribution = [value.text for value in th]
print(distribution)

## 링크 제작
href_b = th[0].attrs["href"]
dfh = pd.DataFrame()
dfh['Nhr'] = th[0].attrs['href']
while(i<len(th)):
    href_b = th[i].attrs["href"]
    href_b = 'namu.wiki' + href_b
    dfh.loc[i] = [href_b]
    i+=1