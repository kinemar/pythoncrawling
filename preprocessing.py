import pandas as pd
import crawling as cw

## 데이터 관련 링크 뽑아오기
board_game_list = pd.DataFrame(cw.distribution)
board_game_list['href'] = cw.dfh['Nhr']
board_game_list

## 데이터 전처리
board_game_list1 = board_game_list.iloc[77:]
board_game_list1 = board_game_list1.rename(columns={0:'name'})
board_game_list1.index = board_game_list1['name']
distribution = cw.distribution[77:]
print(board_game_list1)