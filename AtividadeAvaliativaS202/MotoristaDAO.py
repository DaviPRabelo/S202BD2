from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel:
    def __init__(self, database):
        self.db = database

    def create_motorist(self, nome:str, idade:int, nota:int, corrida):
        try:
            res = self.db.collection.insert_one({"Nome":nome,"Idade":idade,"Nota":nota, "corridas": corrida})
            print(f"Motorista criado. Id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorist: {e}")
            return None

    def read_motorist(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading Motorist: {e}")
            return None

    def update_corrida(self, id: str, corrida):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$push": {"corridas": corrida}})
            print(f"Lista de corridas atualizado: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating Motorist: {e}")
            return None
        
    def update_name_motorist(self, id: str, nome:str):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"Nome": nome}})
            print(f"Motorista atualizado: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating Motorist: {e}")
            return None

    def update_age_motorist(self, id: str, idade:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": { "Idade": idade}})
            print(f"Motorista atualizado: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None


    def delete_motorist(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorist: {e}")
            return None