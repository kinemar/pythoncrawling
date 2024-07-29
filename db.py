## 인증서 및 파이몽고 호출
from pymongo.mongo_client import MongoClient
import certifi

## 몯고DB 연결

client = MongoClient("mongodb+srv://tmddn342:V3lwJ8e5ELCnM2w8@cluster0.rr8s7j4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile = certifi.where())

## db 핑 테스트
try:
    client.admin.command('ping')
    print("db에 연결되었습니다.")
except Exception as e:
    print(e)

db = client['db']
collection = db['users']
