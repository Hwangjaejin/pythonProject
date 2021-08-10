from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert
doc = {'name':'jaejin','age':28}
db.users.insert_one(doc)

# find
same_ages = list(db.users.find({'age':21},{'_id':False})) # _id 값은 가져오지 말아라
same_ages = list(db.users.find({},{'_id':False}))
for person in same_ages:
    print(person)

# find one
user = db.users.find_one({'name':'bobby'})
print(user)

# update one
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# delete one
db.users.delete_one({'name':'bobby'})

