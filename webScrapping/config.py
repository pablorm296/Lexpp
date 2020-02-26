import logging
import datetime
import pymongo
import sys

class LexppConfig:
    def __init__(self, logFile, logLevel, targetClient, targetDB, targetCollection):
        
        # Iniciar bitácora
        self.initLog(logFile, logLevel)

        # Iniciar base de datos
        self.initMongo(targetClient, targetDB, targetCollection)

    # Función para inicializar la bitácora
    def initLog(self, logFile, logLevel):
        # Definimos bitácora
        self.logger = logging.getLogger()
        # Definimos nivel de registro
        self.logger.setLevel(logLevel)
        # Definimos formato
        logFormatter = logging.Formatter("%(levelname)-8s|%(asctime)s|%(module)-10s|%(message)s", "%Y-%m-%d %H:%M:%S")
        # Definimos handlers para consola y archivo
        logFileHandler = logging.FileHandler(logFile)
        logFileHandler.setFormatter(logFormatter)
        logFileHandler.setLevel(logLevel)
        logConsoleHandler = logging.StreamHandler(sys.stdout)
        logConsoleHandler.setFormatter(logFormatter)
        logConsoleHandler.setLevel(logLevel)
        # Agregamos handlers
        self.logger.addHandler(logConsoleHandler)
        self.logger.addHandler(logFileHandler)

    # Función para inicializar la conexión a la base de datos
    def initMongo(self, targetClient, targetDB, targetCollection):
        # Creamos dos diccionarios: uno con bases de datos y otro con colecciones
        self.myDBs = dict()
        self.myCollections = dict()

        # Abrimos conexión con base de datos
        self.logger.info("Creating MongoDB client...")
        self.myMongoClient = pymongo.MongoClient(targetClient)

        # Si la base existe, cargarla, si no, crearla
        self.logger.info("Connecting to database...")
        dbList = self.myMongoClient.list_database_names()
        if targetDB in dbList:
            self.myDBs[targetDB] = self.myMongoClient[targetDB]
        else:
            self.logger.info("The database does not exist. A new one will be created...")
            self.myDBs[targetDB] = self.myMongoClient[targetDB]

        # Acceder a colección de tesis
        self.logger.info("Connecting to collection...")
        collectionList = self.myDBs[targetDB].list_collection_names()
        if targetCollection in collectionList:
            self.myCollections[targetCollection] = self.myDBs[targetDB][targetCollection]
        else:
            self.logger.info("The collection does not exist. A new one will be created...")
            self.myCollections[targetCollection] = self.myDBs[targetDB][targetCollection]
    
    # Función para cerrar conexión
    def closeMongoClient(self):
        self.myMongoClient.close()
        self.myMongoClient = None
        self.myDBs = None
        self.myCollections = None
        delattr(self, "myMongoClient")
        delattr(self, "myDBs")
        delattr(self, "myCollections")

    # Función para mandar mensaje a la bitácora
    def log(self, level, msg):
        self.logger.log(level, msg)

    # Función para mandar un mensaje debug
    def log_DEBUG(self, msg):
        self.logger.debug(msg)

    # Función para mandar un mensaje info
    def log_INFO(self, msg):
        self.logger.info(msg)

    # Función para mandar un mensaje warning
    def log_WARNING(self, msg):
        self.logger.warning(msg)
        
    # Función para mandar un mensaje critical
    def log_CRITICAL(self, msg):
        self.logger.critical(msg)