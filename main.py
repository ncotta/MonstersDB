from pymongo import MongoClient
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
connection = f"mongodb+srv://nikcotta:{PASSWORD}@cluster0.jipt799.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)
