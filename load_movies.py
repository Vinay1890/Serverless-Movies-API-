import json
from pymongo import MongoClient

# Connection string to your MongoDB (or CosmosDB) instance
connection_string = "mongodb://movies-db-account:Oy9jia97GXUEsBpAlggXaHJiPqrlCqNeQ4lvxJxROLpw1EQWVR3tw9D4uQ9b4JTAprf6XhEhih14ACDbVQNb9w==@movies-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@movies-db-account@"

# Connect to the MongoDB cluster
client = MongoClient(connection_string)

# Access the database and collection
db = client['MoviesDB']
collection = db['movies']

# Load data from JSON file
with open('movies.json', 'r') as file:
    movies = json.load(file)

# Insert data into the collection
collection.insert_many(movies)

print("Movies have been successfully loaded into the database.")
