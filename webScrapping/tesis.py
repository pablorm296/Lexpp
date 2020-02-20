from LexppScrapper.LexppScrapper import LexppScrapper
import logging
import datetime
import requests
import pymongo
import re
import sys

#Definimos bitácora
logger = logging.getLogger()
#Definimos nivel de registro
logger.setLevel(logging.INFO)
#Definimos formato
logFormatter = logging.Formatter("%(levelname)-8s|%(asctime)s|%(module)-10s|%(message)s", "%Y-%m-%d %H:%M:%S")
#Definimos handlers para consola y archivo
todayDate = datetime.date.today().strftime("%Y-%m-%d")
logFileHandler = logging.FileHandler("./logs/tesis_{0}.log".format(todayDate))
logFileHandler.setFormatter(logFormatter)
logFileHandler.setLevel(logging.INFO)
logConsoleHandler = logging.StreamHandler(sys.stdout)
logConsoleHandler.setFormatter(logFormatter)
logConsoleHandler.setLevel(logging.INFO)
#Agregamos handlers
logger.addHandler(logConsoleHandler)
logger.addHandler(logFileHandler)

#Abrimos conexión con base de datos
logger.info("Creating MongoDB client...")
MongoClient = pymongo.MongoClient('mongodb://localhost:27017')

#Si la base existe, cargarla, si no, crearla
logger.info("Connecting to MongoDB database...")
dbList = MongoClient.list_database_names()
if 'tesisSCJN' in dbList:
    myMongoDB = MongoClient["tesisSCJN"]
else:
    logger.info("The database does not exist. A new one will be created...")
    myMongoDB = MongoClient["tesisSCJN"]

#Acceder a colección de tesis
logger.info("Connecting to tesis collection...")
collectionList = myMongoDB.list_collection_names()
if 'tesis' in collectionList:
    tesisCollection = myMongoDB["tesis"]
else:
    logger.info("The collection does not exist. A new one will be created...")
    tesisCollection = myMongoDB["tesis"]

#Nueva instancia de LexppScrapper
myScrapper = LexppScrapper(headless = False)

#Navegamos a la página de tesis
myScrapper.goTo("https://sjf.scjn.gob.mx/sjfsist/paginas/tesis.aspx")

#Ir a los resultados del Pleno, Novena Época
#La página utiliza una función para calcular a qué página de resultados redireccionar
#La función toma como argumentos el id de la instancia y el id de la época (Instancia, Época)
#0, 1 = Instancia Pleno, Novena época
myScrapper.webdriver.execute_script("CalcularEpocaLecturaSecuencial(0, 1);")

#Esperamos
myScrapper.waitUntil(".sec-resultados", "css selector")

#Obtenemos lista de elementos
itemList = myScrapper.getElement(".rubro a", "css selector", multiple = True, continueOnExceptions = False)

#Seleccionamos el primer elemento
firstElement = itemList[0]

#Damos clic en el primer elemento
#Al dar click accederemos al primer resultado de la búsqueda (una Tésis); entonces, podremos navegar a través de estos resultados
firstElement.click()

#Esperamos a que el texto de la tesis se carge
myScrapper.sleep(1)

#Obtenemos número de tesis y total
tesisCounterElement = myScrapper.getElement("lblNavegacion", "id", continueOnExceptions = False)
tesisCounterText = tesisCounterElement.text
tesisCounterMatch = re.findall(r"(\d*)\sde\s(\d*)", tesisCounterText)
current = int(tesisCounterMatch[0][0])
total = int(tesisCounterMatch[0][1])
logger.info("Total tesis number: {0}".format(total))
logger.info("Current tesis number: {0}".format(current))

while current < total:
    
    #Si es la primera página, nos saltamos obtener el número de página
    if current > 1:
        #Obtenemos número de tesis y total
        tesisCounterElement = myScrapper.getElement("lblNavegacion", "id", continueOnExceptions = False)
        tesisCounterText = tesisCounterElement.text
        tesisCounterMatch = re.findall(r"(\d*)\sde\s(\d*)", tesisCounterText)
        current = tesisCounterMatch[0][0]
        total = tesisCounterMatch[0][1]
        logger.info("Current tesis number: {0}".format(current))

    #Obtenemos datos necesarios para hacer la request
    reqParameters = dict()
    reqParameters.update(Url = myScrapper.webdriver.execute_script("return window.location.href;"))
    reqParameters.update(IdSesion = myScrapper.webdriver.execute_script("return IdSession;"))
    reqParameters.update(IdActual = myScrapper.webdriver.execute_script("return $(ObtenerControlesServidor().idActual).val();"))
    reqParameters.update(IdELementos = "")
    reqParameters.update(NumeroElementos = "20")
    reqParameters.update(Pagina = "0")
    reqParameters.update(tesisDesmarcadas = "")
    reqParameters.update(Desmarcar = 0)
    logger.info("Parámetros de solicitud: {0}".format(reqParameters))

    #Mandamos la request
    tesisDataRespose = requests.post("https://sjf.scjn.gob.mx/sjfsist/Servicios/wsTesis.asmx/ObtenerDetalle", json = reqParameters)
    tesisDataJson = tesisDataRespose.json()
    tesisDataJson = tesisDataJson.get("d")
    tesisDataJson = tesisDataJson.get("Tesis")

    #Guardamos la tesis
    tesisCollection.insert_one(tesisDataJson)

    #Verificamos que no sea la última página
    if current < total:
        #Damos clic para avanzar a la siguiente página
        myScrapper.clickOn("imgSiguiente", "id", continueOnExceptions = False)

    #Esperamos a que el texto de la tesis se carge
    myScrapper.sleep(1)

#Cerramos la conexión de Mongo
MongoClient.close()

#Matamos el webdriver
myScrapper.killWebDriver()