import pymongo

class Database(object):

    DATABASE = None
    URI = "mongodb://localhost:27017"

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
