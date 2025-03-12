from database import Database
from WriteAjson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()



def Pokedex(func, db):
    _db = db
    if func == 0:
        fire = db.collection.find({"type": {'$in': ['Fire']}})
        writeAJson(fire,"fire")
    elif func ==1:
        spwcnc = db.collection.find({"spawn_chance": {"$gt": 0.2, "$lt": 0.4}})
        writeAJson(spwcnc, "spwcnc")
    elif func == 2:
        Grass = db.collection.find({"weaknesses": {'$all': ['Grass']}})
        writeAJson(Grass, "grassweaknesses")
    elif func == 3:
        poisonandFlying = db.collection.find({"type": {'$in': ['Poison','Flying']}})
        writeAJson(poisonandFlying, "poisonFly")
    elif func == 4:
        _2weak = db.collection.find({"weaknesses": {"$size": 2}})
        writeAJson(_2weak, "2weaknesses")


Pokedex(0,db)
Pokedex(1,db)
Pokedex(2,db)
Pokedex(3,db)
Pokedex(4,db)