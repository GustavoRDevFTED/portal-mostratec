import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

database = client[os.getenv("MONGO_DATABASE", "mostratec")]

def get_database():
    return database