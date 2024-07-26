## 인증서 및 파이몽고 호출
from pymongo.mongo_client import MongoClient
import certifi

## 몯고DB 연결

client = MongoClient("mongodb+srv://[주소]", tlsCAFile = certifi.where())

## db 핑 테스트
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['db']
collection = db['users']
