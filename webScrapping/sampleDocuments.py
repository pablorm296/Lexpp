import pymongo
import json

# Abrir conexión con el cliente
client = pymongo.MongoClient("mongodb://localhost:27017")

# Ir a la base de datos
db = client["LexppLibrary_SCJN"]

# Ir a la colección de expedientes
collection = db["expedientes"]

# Hacer un muestreo aleatorio
comando = collection.aggregate([
    {"$project": {"_id": 0}},
    {"$sample": {"size": 3}}
])

# Obtener resultados
muestra = list(comando)

# Guardar la muestra
with open("muestra_documentos.json", "w") as targetFile:
    json.dump(muestra, targetFile)