from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://saurabhjoshi7869:3wqqUZe6D9ypEUcb@streamlit-shorturl-app.s8bdj.mongodb.net/?retryWrites=true&w=majority&appName=streamlit-shorturl-app"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)