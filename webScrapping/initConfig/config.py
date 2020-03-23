import logging
import datetime
import pymongo
import sys

class LexppConfig:
    def __init__(self, logFile, logLevel, mode, targetClient, targetDB = None, targetCollection = None):
        
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

        # Log info
        self.logger.info("Initializing logging config...")

    # Función para inicializar la conexión a la base de datos
    def initMongo(self, targetClient, targetDB, targetCollection):
        # Log info
        self.logger.info("Initializing MongoDB connection...")

        # Verificamos argumentos
        if targetDB is None and targetCollection is not None:
            raise ValueError("If targetCollection is specified, please also use targetDB")
        if targetCollection is None and targetDB is not None:
            raise ValueError("If targetDB is specified, please also use targetCollection")
        # Creamos dos diccionarios: uno con bases de datos y otro con colecciones
        self.myDBs = dict()
        self.myCollections = dict()

        # Abrimos conexión con cliente de Mongo
        self.logger.info("Creating MongoDB client...")
        self.myMongoClient = pymongo.MongoClient(targetClient)

        # Si el usuario especifico base de datos y colección
        if targetDB is not None and targetCollection is not None:
            # Si la base existe, cargarla, si no, crearla
            self.logger.info("Connecting to database...")
            dbList = self.myMongoClient.list_database_names()
            if targetDB in dbList:
                self.myDBs[targetDB] = self.myMongoClient[targetDB]
            else:
                self.logger.info("The database does not exist. A new one will be created...")
                self.myDBs[targetDB] = self.myMongoClient[targetDB]

            # Registramos base de datos como última base
            self.lastMongoDB = targetDB

            # Creamos una string para registrar la colección
            targetCollectionstr = "{0}/{1}".format(targetDB, targetCollection)

            # Acceder a colección de tesis
            self.logger.info("Connecting to collection...")
            collectionList = self.myDBs[targetDB].list_collection_names()
            if targetCollection in collectionList:
                self.myCollections[targetCollectionstr] = self.myDBs[targetDB][targetCollection]
            else:
                self.logger.info("The collection does not exist. A new one will be created...")
                self.myCollections[targetCollectionstr] = self.myDBs[targetDB][targetCollection]

            # Registramos colección como última
            self.lastMongoCollection = targetCollectionstr
    
    # Función para cerrar conexión
    def closeMongoClient(self):
        # Log info
        self.logger.info("Closing mongodb connection...")

        # Primero, faciar bases de datos/colecciones y después eliminar los atributos
        self.myMongoClient.close()
        self.myMongoClient = None
        self.myDBs = None
        self.myCollections = None
        delattr(self, "myMongoClient")
        delattr(self, "myDBs")
        delattr(self, "myCollections")

    # Función para abrir nueva conexión a colección
    def openNewCollection(self, targetCollection, targetDB = "__last", overWrite = False):
        # Si el usuario quiere usar la última base de datos
        if targetDB == "__last":
            targetDB = self.lastMongoDB

        # Creamos una string para registrar la colección
        targetCollectionstr = "{0}/{1}".format(targetDB, targetCollection)

        # Log info
        self.logger.info("Opening new connection to collection {0}...".format(targetCollectionstr))

        # Si la colección de datos especificada ya esta abierta
        if targetCollectionstr in self.myCollections and not overWrite:
            self.logger.warning("The collection is already open!")
            raise TypeError("The collection is already open!")

        # Si la base no está registrada
        if targetDB not in self.myDBs:
            # Si la base existe, cargarla, si no, crearla
            self.logger.info("Connecting to database...")
            dbList = self.myMongoClient.list_database_names()
            if targetDB in dbList:
                self.myDBs[targetDB] = self.myMongoClient[targetDB]
            else:
                self.logger.info("The database does not exist. A new one will be created...")
                self.myDBs[targetDB] = self.myMongoClient[targetDB]

            # Registramos base de datos como última base
            self.lastMongoDB = targetDB

        # Acceder a colección especificada
        self.logger.info("Connecting to collection...")
        collectionList = self.myDBs[targetDB].list_collection_names()
        if targetCollection in collectionList:
            self.myCollections[targetCollectionstr] = self.myDBs[targetDB][targetCollection]
        else:
            self.logger.info("The collection does not exist. A new one will be created...")
            self.myCollections[targetCollectionstr] = self.myDBs[targetDB][targetCollection]

        # Registramos colección como última
        self.lastMongoCollection = targetCollectionstr

    # Función para abrir nueva conexicón a base de datos
    def openNewDB(self, targetDB, overWrite = False):
        # Log info
        self.logger.info("Opening new connection to db {0}...".format(targetDB))

        # Si la base de datos especificada ya esta abierta
        if targetDB in self.myDBs and not overWrite:
            self.logger.warning("The database is already open!")
            raise TypeError("The database is already open!")

        # Si la base existe, cargarla, si no, crearla
        self.logger.info("Connecting to database...")
        dbList = self.myMongoClient.list_database_names()
        if targetDB in dbList:
            self.myDBs[targetDB] = self.myMongoClient[targetDB]
        else:
            self.logger.info("The database does not exist. A new one will be created...")
            self.myDBs[targetDB] = self.myMongoClient[targetDB]

        # Registramos base de datos como última base
        self.lastMongoDB = targetDB

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