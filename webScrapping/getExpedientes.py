from LexppScrapper.LexppScrapper import LexppScrapper
from config import LexppConfig
import argparse
import logging
import datetime
import requests
import pymongo
import re
import sys



def getExpedientes(arguments):

    # Convertir nivel de verbose
    if arguments.verbose == "debug":
        log_level = logging.DEBUG
    elif arguments.verbose == "normal":
        log_level = logging.INFO
    elif arguments.verbose == "none":
        log_level = logging.WARNING

    #Fecha del día de hoy (para el archivo de log)
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    #Inicializamos configuración
    myConfig = LexppConfig(logFile = "./logs/expedientes_{0}.log".format(todayDate), logLevel = log_level, targetClient = 'mongodb://localhost:27017', targetDB = "sentenciasSCJN", targetCollection = "sentencias")

    # Dependiendo del tipo de modo, verificar que el usuario haya ingresado otros argumentos
    myConfig.log_DEBUG("Verificando argumentos...")
    if arguments.modo == "tipoAsunto":
        # El ususario no puso el argumento necesario
        if arguments.tipoAsunto is None:
            error_msg = "Falta especificar el tipo de asunto!"
            myConfig.log_CRITICAL(error_msg)
            raise Exception(error_msg)
    elif arguments.modo == "orgRadicacion":
        # El ususario no puso el argumento necesario
        if arguments.orgRadicacion is None:
            error_msg = "Falta especificar el órgano de radicación!"
            myConfig.log_CRITICAL(error_msg)
            raise Exception(error_msg)
    elif arguments.modo == "ministro":
        # El ususario no puso el argumento necesario
        if arguments.ministro is None:
            error_msg = "Falta especificar el ministro!"
            myConfig.log_CRITICAL(error_msg)
            raise Exception(error_msg)
    elif arguments.modo == "especifico":
        # El ususario no puso el argumento necesario
        if arguments.expedienteInfo is None:
            error_msg = "Falta especificar ID de asunto o ID de expediente"
            myConfig.log_CRITICAL(error_msg)
            raise Exception(error_msg)

    #Nueva instancia de LexppScrapper
    myScrapper = LexppScrapper(headless = False)

#Navegamos a la página de sentencias
#myScrapper.goTo("https://sjf.scjn.gob.mx/sjfsist/paginas/tesis.aspx") #COMMENTED: RECUPERAR PROGRSO

#Ir a los resultados del Pleno, Novena Época
#La página utiliza una función para calcular a qué página de resultados redireccionar
#La función toma como argumentos el id de la instancia y el id de la época (Instancia, Época)
#0, 1 = Instancia Pleno, Novena época

#myScrapper.webdriver.execute_script("CalcularEpocaLecturaSecuencial(0, 1);") #COMMENTED: RECUPERAR PROGRSO

#Esperamos
#myScrapper.waitUntil(".sec-resultados", "css selector") #COMMENTED: RECUPERAR PROGRSO

#Obtenemos lista de elementos
#itemList = myScrapper.getElement(".rubro a", "css selector", multiple = True, continueOnExceptions = False) #COMMENTED: RECUPERAR PROGRSO

#Seleccionamos el primer elemento
#firstElement = itemList[0] #COMMENTED: RECUPERAR PROGRSO

#Damos clic en el primer elemento
#Al dar click accederemos al primer resultado de la búsqueda (una Tésis); entonces, podremos navegar a través de estos resultados
#firstElement.click() #COMMENTED: RECUPERAR PROGRSO

#Esperamos a que el texto de la tesis se carge
#myScrapper.sleep(1) #COMMENTED: RECUPERAR PROGRSO

myScrapper.goTo("https://sjf.scjn.gob.mx/sjfsist/paginas/DetalleGeneralV2.aspx?Epoca=100800000000000&Apendice=10000000000&Expresion=&Dominio=Rubro,Texto&TA_TJ=2&Orden=1&Clase=DetalleTesisBL&NumTE=3556&Epp=20&Desde=-100&Hasta=-100&Index=161&InstanciasSeleccionadas=&ID=200037&Hit=3236&IDs=200055,200054,200053,200051,200050,200049,200048,200047,200046,200045,200044,200043,200040,200039,200038,200037,200036,200035,200034,200033&tipoTesis=&Semanario=0&tabla=&Referencia=&Tema=")

#Obtenemos número de tesis y total
tesisCounterElement = myScrapper.getElement("lblNavegacion", "id", continueOnExceptions = False)
tesisCounterText = tesisCounterElement.text
tesisCounterMatch = re.findall(r"(\d*)\sde\s(\d*)", tesisCounterText)
current = int(tesisCounterMatch[0][0])
total = int(tesisCounterMatch[0][1])
tesisConfig.log(logging.INFO, "Total tesis number: {0}".format(total))
tesisConfig.log(logging.INFO, "Current tesis number: {0}".format(current))

while current < total:

    #Si es la primera página, nos saltamos obtener el número de página
    if current > 1:
        #Obtenemos número de tesis y total
        tesisCounterElement = myScrapper.getElement("lblNavegacion", "id", continueOnExceptions = False)
        tesisCounterText = tesisCounterElement.text
        tesisCounterMatch = re.findall(r"(\d*)\sde\s(\d*)", tesisCounterText)
        current = int(tesisCounterMatch[0][0])
        total = int(tesisCounterMatch[0][1])
        tesisConfig.log(logging.INFO, "Current tesis number: {0}".format(current))

    #Obtenemos datos necesarios para hacer la request
    reqParameters = dict()
    reqParameters.update(Url = myScrapper.webdriver.execute_script("return window.location.href;"))
    reqParameters.update(IdSesion = myScrapper.webdriver.execute_script("return IdSession;"))
    reqParameters.update(IdActual = myScrapper.webdriver.execute_script("return $(ObtenerControlesServidor().idActual).val();"))
    reqParameters.update(IdELementos = "")
    reqParameters.update(NumeroElementos = "20")
    reqParameters.update(Pagina = myScrapper.webdriver.execute_script("return $(ObtenerControlesServidor().Pagina).val()"))
    reqParameters.update(tesisDesmarcadas = "")
    reqParameters.update(Desmarcar = 0)
    tesisConfig.log(logging.INFO, "Parámetros de solicitud: {0}".format(reqParameters))

    #Mandamos la request
    tesisDataRespose = requests.post("https://sjf.scjn.gob.mx/sjfsist/Servicios/wsTesis.asmx/ObtenerDetalle", json = reqParameters)
    tesisDataJson = tesisDataRespose.json()
    tesisDataJson = tesisDataJson.get("d")
    tesisDataJson = tesisDataJson.get("Tesis")

    #Guardamos la tesis
    tesisConfig.myCollections["tesis"].insert_one(tesisDataJson)

    #Verificamos que no sea la última página
    if current < total:
        #Damos clic para avanzar a la siguiente página
        myScrapper.clickOn("imgSiguiente", "id", continueOnExceptions = False)

    #Esperamos a que el texto de la tesis se carge
    myScrapper.sleep(1)

#Cerramos la conexión de Mongo
tesisConfig.closeMongoClient()

#Matamos el webdriver
myScrapper.killWebDriver()

if __name__ == "__main__":
    # Inicializar parser para los argumentos
    main_parser = argparse.ArgumentParser(
        description="Un script para buscar y escanear expedientes de la Suprema Corte de Justicia de la Nación")
    main_parser.add_argument("-m", "--modo", default="all", type=str, choices=["todo", "tipoAsunto", "orgRadicacion", "ministro", "especifico"],
                            help="¿Qué rutina debe realizar el script? Un escaneo completo del sistema (todo),"
                            " escanear por 'tipo de asunto' (tipoAsunto), escanear por tipo de 'órgano de radicación' (orgRadicacion), escanear por"
                            " 'ministro' (ministro), o buscar un expediente específico (especifico).", required=True)
    # Argumento: tipo de asunto
    main_parser.add_argument("--tipoAsunto", type=str,
                            help="Si MODO == 'tipoAsunto', identificador del tipo de asunto a escanear.", required=False)
    # Argumento: órgano de radicación
    main_parser.add_argument("--orgRadicacion", type=str, choices=["primera", "segunda", "pleno"],
                            help="Si MODO == 'orgRadicacion', identificador del órgano de radicación.", required=False)
    # Argumento: ministro que lleva el asunto
    main_parser.add_argument("--ministro", type=str,
                            help="Si MODO == 'ministro', identificador o nombre del ministro que llevó el expediente.", required=False)
    # Argumento: información del expediente que se busca
    main_parser.add_argument("--expedienteInfo", type=str,
                            help="Si MODO == especifico, identificador del expediente (ya sea por ID de expediente o ID de asunto)", required=False)
    # Argumento: opción de mensajes
    main_parser.add_argument("-v", "--verbose", default="debug", required=True,
                            choices=["debug", "normal", "none"], type=str, help="¿Qué mensajes imprimir en la consola? Depuración, normal o ninguno")
    # Argumento: opción al lanzar el explorador
    main_parser.add_argument("-hl", "--headless", default=0,
                            choices=[0, 1], type=int, help="Si se abre una instancia de Firefox, ¿debe ser headless? 1 = Sí, 0 = No")
    # Argumento: ir a la página de resultados
    main_parser.add_argument("-p", "--goToPage", default=1,
                            type=int, help="¿En qué página de resultados iniciar la búsqueda de expedientes?")

    # Obtener argumentos del ususario y parsearlos
    arguments = main_parser.parse_args()

    # Pasar los argumentos a la función principal
    getExpedientes(arguments)