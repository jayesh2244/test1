import pymongo
client = pymongo.MongoClient("mongodb+srv://jayesh:jayesh@cluster1.0wtpo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d ={
    "name":"jayesh",
   "age":"1"
}
db1=client['test1']
coll=db1['test']
coll.insert_one(d)