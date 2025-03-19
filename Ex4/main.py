
from database import Database
from WriteAJason import writeAJson

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

def ProductAnalyzer (number):
    if number == 1:
        totalVendasDia = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}}])
        writeAJson(totalVendasDia, "Quantidade de vendas em um dia")

    elif number == 2:
        produtoMaisVend =  db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit":1}])
        writeAJson(produtoMaisVend,"Produto mais vendido")
    elif number == 3:
        clienteMaisGasto = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}])
        writeAJson(clienteMaisGasto,"Cliente com mais gasto")
    elif number == 4:
        produtoGT1 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total": {"$gt": 1}}}])
        writeAJson(produtoGT1,"Produtos com mais de 1 venda")


a = int(input())

pesquisaMercado = ProductAnalyzer(a)

