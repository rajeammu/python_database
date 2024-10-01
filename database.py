import pymongo

# Create a MongoDB client
myclient = pymongo.MongoClient("mongodb+srv://rajeswari:Raje%401996@cluster0.1jb72.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Access the database
mydb = myclient.python
print("The database exists.")
# Access the collection (ensure the name is correct)
col = mydb.learning  
print("The collection exists.")
# Document to insert
mylist = [
    {
    "name": "ram",
    "age": 22,
    "roll no":12345,
    "dept":"cse",
    "college":"svcet"
},
{
    "name": "raghul",
    "age": 18,
    "roll no":45638,
    "dept":"it",
    "college":"mit"
},
{
    "name": "sajesh",
    "age": 20,
    "roll no":78945,
    "dept":"ece",
    "college":"smvec"
}
]

# Insert the document
res = col.insert_many(mylist)

# Print the inserted ID
# print("Inserted document with ID:", res.inserted_ids)
myquery=col.find().limit(2)
for x in myquery:
    print(x)
