import db

## MongoDB
try:
    db.collection.insert_many(board_game_list1.to_dict('records'))
    print("Data Save Successfully!!")

except Exception as e:
    print("Save Failed...")