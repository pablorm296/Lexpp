from LexppScrapper.LexppScrapper import LexppScrapper
import logging
import datetime
import requests
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

#Nueva instancia de LexppScrapper
myScrapper = LexppScrapper(headless = False)

#Navegamos a la página de tesis
myScrapper.goTo("https://sjf.scjn.gob.mx/sjfsist/paginas/tesis.aspx")

#Ir a los resultados del Pleno, Décima Época
#La página utiliza una función para calcular a qué página de resultados redireccionar
#La función toma como argumentos el id de época y el id de órgano (Pleno, sala)
#0, 0 = Décima época, pleno
myScrapper.webdriver.execute_script("CalcularEpocaLecturaSecuencial(0, 0);")

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

while current < total:
    
    #Si es la primera página, nos saltamos obtener el número de página
    if current > 1:
        #Obtenemos número de tesis y total
        tesisCounterElement = myScrapper.getElement("lblNavegacion", "id", continueOnExceptions = False)
        tesisCounterText = tesisCounterElement.text
        tesisCounterMatch = re.findall(r"(\d*)\sde\s(\d*)", tesisCounterText)
        current = tesisCounterMatch[0][0]
        total = tesisCounterMatch[0][1]

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
    print(tesisDataJson)

    #Damos clic para avanzar a la siguiente página
    myScrapper.clickOn("imgSiguiente", "id", continueOnExceptions = False)

    #Esperamos a que el texto de la tesis se carge
    myScrapper.sleep(2)


#Matamos el webdriver
myScrapper.killWebDriver()