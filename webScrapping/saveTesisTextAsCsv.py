#Este script toma el texto de las sentencias, guardado en la base de datos,
#le quita los tags html y lo guarda como csv

import pymongo
import pandas
from html.parser import HTMLParser

#Funciones para limpiar HTML
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#Abrimos conexión con base de datos
MongoClient = pymongo.MongoClient('mongodb://localhost:27017')
myMongoDB = MongoClient["tesisSCJN"]
tesisCollection = myMongoDB["tesis"]

#Obtener todos los textos
tesisQuery = tesisCollection.find({}, {"Texto": 1, "Rubro": 1, "Ius": 1, "IdEpoca": 1, "_id": 1})
tesisList = list(tesisQuery)

#Convertir en un dataframe
tesisDataFrame = pandas.DataFrame(tesisList)

#Detectamos ids de documentos duplicados
tesisDataFrame = tesisDataFrame[tesisDataFrame.duplicated(["Ius", "IdEpoca"], keep = "first")]

#Eliminar información HTML
tesisDataFrame["Texto"] = tesisDataFrame["Texto"].apply(lambda x: strip_tags(x))
tesisDataFrame["Texto"] = tesisDataFrame["Texto"].apply(lambda x: strip_tags(x))

#Guardar como csv
tesisDataFrame.to_csv("webScrapping/data/tesis.csv", sep = ",", encoding = "utf-8")


