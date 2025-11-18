from pymongo import MongoClient
user = 'root'
password = 'root'

#creating the connection url
connecturl = "mongodb+srv://root:root@mydb.ecnjxsh.mongodb.net/?retryWrites=true&w=majority"

#connecting to the mongodb server
print("Connecting to MongoDB server...")
connection = MongoClient(connecturl)

#get database list
print("Getting database list...")
dbs = connection.list_database_names()

#print the database names

for db in dbs:
    print(db)
print("Closing the connection to the MongoDB server...")

#closing the connection
connection.close()
print("Connection closed.")