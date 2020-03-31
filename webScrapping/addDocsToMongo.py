import argparse
import logging
import datetime
import pymongo
import json
import os

# Main routine
def main(arguments):
    # Extraer argumentos
    targetFile = arguments.file
    targetLibrary = arguments.library
    targetCollection = arguments.collection

    # Logging info
    logging.debug("Procesando {0}".format(targetFile))

    # Verificar que el archivo no sea un directorio
    if os.path.isdir(targetFile):
        raise FileNotFoundError("El archivo {0} es un directorio!".format(targetFile))
    
    # Verificar que el archivo exista
    if not os.path.isfile(targetFile):
        raise FileNotFoundError("El archivo {0} no existe!".format(targetFile))

    # Creamos un cliente de pymongo
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017")

    # Verificar que la librería y la coleccipón existan
    dbList = mongoClient.list_database_names()
    if targetLibrary not in dbList:
        raise IOError("La biblioteca {0} no existe!".format(targetLibrary))
    
    # Conectar a la base 
    mongoDB = mongoClient[targetLibrary]

    # Verificar que la colección existe
    collectionList = mongoDB.collection_names()
    if targetCollection not in collectionList:
        raise IOError("La colección {0} no existe!".format(targetCollection))

    # Conectar a la colección
    mongoCollection = mongoDB[targetCollection]

    # Abrimos el archivo
    with open(targetFile, "r") as f:
        targetFileContent = json.load(f)

    # Definir nombre del campo con el LexppId de la biblioteca
    LexppIdField = "Lexpp_{0}Id".format(targetCollection)

    # Extraer LexppId del expediente
    LexppId = targetFile["LexppId"]

    # Extraer LexppId del expediente (coleccion)
    LexppId_colection = targetFile[LexppIdField]

    # Buscar LexppId en la biblioteca
    matchLexppId = mongoCollection.find_one(
        {"LexppId": LexppId}
    )

    # Buscar LexppId en la biblioteca
    matchLexppCollectionId = mongoCollection.find_one(
        {LexppIdField: LexppId_colection}
    )

    # Si ninguno de los está
    if matchLexppCollectionId is None and matchLexppId is None:
        logging.debug("El documento no está en la base de datos!")
   

if __name__ == "__main__":
    # Init logging
    logging.basicConfig(level = logging.DEBUG)

    # Inicializar parser para los argumentos
    main_parser = argparse.ArgumentParser(
        description="Un script para agregar expdientes y documentos a la base de datos de MongoDB")
    # Argumento: nombre del archivo
    main_parser.add_argument("-f", "--file", type=str,
                            help="Path del expediente o documento.", required=True)
    # Argumento: nombre de la biblioteca Lex++
    main_parser.add_argument("--library", type=str,
                            help="Biblioteca de Lex++ en el que se guardará el expediente o documento.", required=True)
    # Argumento: nombre de la colección en dicha biblioteca de Lex++
    main_parser.add_argument("--collection", type=str,
                            help="Colección de la biblioteca en el que se guardará el expediente o documento.", required=True)

    # Obtener argumentos del ususario y parsearlos
    arguments = main_parser.parse_args()

    # Pasar los argumentos a la función principal
    main(arguments)
