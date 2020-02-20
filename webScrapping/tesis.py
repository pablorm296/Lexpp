from LexppScrapper.LexppScrapper import LexppScrapper
import logging
import datetime
import sys

#Definimos bitácora
logger = logging.getLogger()
#Definimos nivel de registro
logger.setLevel(logging.INFO)
#Definimos formato
logFormatter = logging.Formatter("%(levelname)-8s|%(asctime)s|%(module)s|%(message)s", "%Y-%m-%d %H:%M:%S")
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
myScrapper.sleep(5)

#Matamos el webdriver
myScrapper.killWebDriver()