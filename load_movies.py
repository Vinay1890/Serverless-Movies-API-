import json
from pymongo import MongoClient

# Connection string to your MongoDB (or CosmosDB) instance
connection_string = "your_cosmos_db_connection_string"

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
