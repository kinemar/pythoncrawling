## 라이브러리 호출
### DB라이브러리는 직접 db.py file로 먼저 생성 후 테스트
import pandas as pd

search_DF = pd.DataFrame


search_engine = input("검색 엔진을 정해주세요 : ")
if search_engine == '네이버' or search_engine == "naver":
    import naver_crawling as nac
    search_DF = nac.search_DF
    search_data = nac.search_target

elif search_engine == '구글' or search_engine == "google":
    import google_crawling as gac
    distribution = gac.search_DF
    search_data = gac.search_target