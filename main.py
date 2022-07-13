from pymongo import MongoClient
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
connection = f"mongodb+srv://nikcotta:{PASSWORD}@cluster0.cwjfqao.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)

db = client["monsters"]
collection = db["monsters"]

# FIXME: id increment


def getNumMonsters():
    return collection.count_documents({})


def insert(_id, name, difficulty, stats, dispo, desc):
    # testPost = {"_id": 0, "name:": "Tim", "score": 5}
    # collection.insert_one(testPost)
    # collection.insert_many([testPost, testPost])
    post = {"_id": _id, "name": name, "difficulty": difficulty, "stats": stats,
            "disposition": dispo, "description": desc}

    try:
        collection.insert_one(post)
    except Exception as e:
        print(e)
        print("Could not insert")


def find(category, query, limit=1):
    # results = collection.find({"name": "Tim"})
    # for result in results:
    #     print(result["_id"])

    # results = collection.find_one({"name": "Tim"})
    # print(results)
    results = collection.find({category: query})
    for i in range(limit):
        print(results[i])


def delete():
    # results = collection.delete_one({"_id": 0})
    # print("deletion successful")
    pass  # FIXME


def update():
    # results = collection.update_one({"_id":0}, {"$set": {"name": "tim" }})
    pass  # FIXME
