import pymongo

Host="mongodb://localhost:27017/"

client = pymongo.MongoClient(Host)
mydb = client["mydatabase"]

mycol = mydb["customers"]

# Insert a document into the "customers" collection
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

# Print the inserted document's ID
print(x.inserted_id)
