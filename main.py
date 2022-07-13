from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
connection = f"mongodb+srv://nikcotta:{PASSWORD}@cluster0.cwjfqao.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)

collection = client["monsters"]["monsters"]

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
        print(f"{name} data added")
    except Exception as e:
        print(e)
        print(f"Could not add {name}")


def find(category, query, limit=1):
    # results = collection.find({"name": "Tim"})
    # for result in results:
    #     print(result["_id"])

    # results = collection.find_one({"name": "Tim"})
    # print(results)
    try:
        results = collection.find({category: query})
        print(f"Scanned {getNumMonsters()} entries and found: ")
        for i in range(limit):
            print(results[i])
    except IndexError:
        print("Nothing. Could not find specified monster")


def delete():
    # results = collection.delete_one({"_id": 0})
    # print("deletion successful")
    pass  # FIXME


def delete_all():
    response = input("Are you sure you want to delete every entry? (y/n): ")
    if response.strip() == "y":
        collection.delete_many({})
    else:
        print("Deletion cancelled")


def update():
    # results = collection.update_one({"_id":0}, {"$set": {"name": "tim" }})
    pass  # FIXME


if __name__ == '__main__':
    find("_id", 1)

