from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
movie = db.movies.find_one({'title': '월-E'})

print(movie['star'])
