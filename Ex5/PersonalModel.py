from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, titulo:str, autor: str, ano:int, preco:int):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco":preco})
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_book_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Person found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_book_titulo(self, id: str, titulo:str):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def update_book_autor(self, id: str, autor: str):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": { "autor": autor}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def update_book_ano(self, id: str, ano:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": { "ano": ano}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def update_book_preco(self, id: str, titulo:str, autor: str, ano:int, preco:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"preco":preco}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def delete_book(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None