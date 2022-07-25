import pymongo
client = pymongo.MongoClient("mongodb+srv://danish:9319977069Da@danish.yoett.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"danish",
    "lname":"joher",
    "email" : "danishjoher@gmail.com"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)