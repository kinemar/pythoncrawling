import db

# DB 조회
data = db.collection.find()

#조회된 데이터 출력
for document in data:
    print(document)
