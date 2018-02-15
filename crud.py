from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

user = {
    "name": "Santu",
    "age" : 18
}

db = client.test
post = db.test
# post.insert_one(user)
for user in post.find():
    pprint.pprint(user)
