import db
import preprocessing as PrP

## MongoDB
try:
    db.collection.insert_many(PrP.board_game_list1.to_dict('records'))
    print("데이터가 저장되었습니다.")

except Exception as e:
    print("저장 실패하였습니다.")