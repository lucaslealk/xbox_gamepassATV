from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["XboxGamePass"]
colecao = db["gamepass"]

#CONEXÃO COM MONGODB
