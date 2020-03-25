import argparse
import logging
import datetime
import pymongo
import tika
import os

def main(arguments):
    # Extraer argumentos
    targetFile = arguments.file
    targetLibrary = arguments.library
    targetCollection = arguments.collection

    # Logging info
    logging.info("Procesando {0}".format(targetFile))
    
    # Verificar que el archivo exista
    if not os.path.isfile(targetFile):
        raise FileNotFoundError("El archivo {0} no existe".format(targetFile))

    # Creamos un cliente de pymongo
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017")

    # Verificar que la librería y la coleccipón existan
    dbList = mongoClient.list_database_names()
    if targetLibrary not in dbList:
        raise IOError("La biblioteca {0} no existe".format(targetLibrary))
    
    # Conectar a la base 
    mongoDB = mongoClient[targetLibrary]

    # Verificar que la colección existe
    collectionList = mongoDB.collection_names()
    if targetCollection not in collectionList:
        raise IOError("La colección {0} no existe".format(targetCollection))

    # Conectar a la colección
    mongoCollection = mongoDB[targetCollection]

    # Tika test
    logging.info("Tika test")



if __name__ == "__main__":
    # Init logging
    logging.basicConfig(level = logging.INFO)

    # Inicializar parser para los argumentos
    main_parser = argparse.ArgumentParser(
        description="Un script para extraer contenido de un archivo y agregarlo a la metadescripción del documento en la base de datos de MongoDB")
    # Argumento: nombre del archivo
    main_parser.add_argument("-f", "--file", type=str,
                            help="Path del archivo del cual se va a extraer el contenido. El nombre del archivo debe contener la LexppId que identifica al documento en su biblioteca correspondiente", required=True)
    # Argumento: nombre de la biblioteca Lex++
    main_parser.add_argument("--library", type=str,
                            help="Biblioteca de Lex++ en el que se encuentra la metadescripción del documento al que corresponde el archivo.", required=True)
    # Argumento: nombre de la colección en dicha biblioteca de Lex++
    main_parser.add_argument("--collection", type=str,
                            help="Colección de la biblioteca en el que se encuentra la metadescripción del documento al que corresponde el archivo.", required=True)


    # Obtener argumentos del ususario y parsearlos
    arguments = main_parser.parse_args()

    # Pasar los argumentos a la función principal
    main(arguments)