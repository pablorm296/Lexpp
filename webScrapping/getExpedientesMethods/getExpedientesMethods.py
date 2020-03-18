from LexppScrapper.LexppScrapper import LexppScrapper
from initConfig.config import LexppConfig
from datetime import datetime
import requests
import re
import uuid
import hashlib
import json

# Clase para obtener detalles del Asunto
class expediente:
    def __init__(self, idAsunto, idExpediente, config: LexppConfig):
        # Guardamos el id del expediente e id del asunto
        self.idAsunto = idAsunto
        self.idExpediente = idExpediente
        # Generamos un identificador único para el documento
        # Uno para control dentro de la biblioteca de expedientes y otro para control dentro de Lexpp
        self.LexppId = str(uuid.uuid4())
        self.LexppId_Expedientes = str(uuid.uuid4())
        #Guardamos el objeto de configuración
        self.config = config

        # Log info
        self.config.log_INFO("Expediente creado! idAsunto:{0}| idExpediente:{1}".format(idAsunto, idExpediente))
        # Log debug
        self.config.log_DEBUG("Expediente creado! LexppId:{0}| LexppId_Expedientes:{1}".format(self.LexppId, self.LexppId_Expedientes))
        # Inicializamos el contenido del expediente
        self.Content = dict()
        # Empezamos a guardar el contenido del expediente
        self.getDetalleAsunto()
        self.getResolutivoGeneral()
        # Si existe 
 
    # Obtiene contenido del expediente
    def getContent(self):
        return self.Content

    # Obtiene detalles del asunto
    def getDetalleAsunto(self):
        # Obtenemos la url objetivo a partir de la base de datos
        targetUrl = self.config.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "obtieneDetalleAsunto"})
        # Verificamos que la URL esté registrada en la base de datos
        if targetUrl is None:
            error_msg = "La URL no está registrada!"
            self.config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)

        # Obtenemos la versión de la URL que puede formatearse con strings de python
        targetUrlFormatted = targetUrl["formatted"]
        pURLpar = targetUrl["pURL"]

        # Creamos un objeto con los parámetros que vamos a enviar al servidor
        jsonPayload = {"pAsuntoID": self.idAsunto, "bandera": 0, "pURL": pURLpar}

        # Enviamos solicitud al servidor
        response = requests.post(targetUrlFormatted, json = jsonPayload)

        # Calculamos md5 de la respuesta
        md5_encoder = hashlib.md5()
        response_json = response.json()
        # Los datos vienen en el campo {"d": "..."} Es importante señalar que el campo "d" es un campo de texto y no un objeto directamente interpretado como json
        response_json = response_json.get("d", "")
        md5_encoder.update(response_json.encode('utf-8'))
        # Obtenemos un objeto a partir de la respuesta
        response_json_parsed = json.loads(response.json().get("d", {}))

        detalleAsunto = {"data": response_json_parsed, "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.detalleAsunto = detalleAsunto
        self.Content.update({"detalleAsunto": self.detalleAsunto})

        #Regresamos true
        return True

    # Obtiene resolutivo general
    def getResolutivoGeneral(self):

        # Obtenemos la url objetivo a partir de la base de datos
        targetUrl = self.config.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "obtieneResolutivoGeneral"})
        # Verificamos que la URL esté registrada en la base de datos
        if targetUrl is None:
            error_msg = "La URL no está registrada!"
            self.config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)

        # Obtenemos la versión de la URL que puede formatearse con strings de python
        targetUrlFormatted = targetUrl["formatted"]
        pURLpar = targetUrl["pURL"]

        # Creamos un objeto con los parámetros que vamos a enviar al servidor
        jsonPayload = {"pAsuntoID": self.idAsunto, "bandera": 0, "pURL": pURLpar}

        # Enviamos solicitud al servidor
        response = requests.post(targetUrlFormatted, json = jsonPayload)

        # Calculamos md5 de la respuesta
        md5_encoder = hashlib.md5()
        response_json = response.json()
        # Los datos vienen en el campo {"d": "..."} Es importante señalar que el campo "d" es un campo de texto y no un objeto directamente interpretado como json
        response_json = response_json.get("d", "")
        md5_encoder.update(response_json.encode('utf-8'))
        # Obtenemos un objeto a partir de la respuesta
        response_json_parsed = json.loads(response.json().get("d", {}))

        resolutivoGeneral = {"data": response_json_parsed, "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.resolutivoGeneral = resolutivoGeneral
        self.Content.update({"resolutivoGeneral": self.resolutivoGeneral})

        #Regresamos true
        return True


# Rutina de inicializacion  
def init(LexppConfig):
    # Abrimos una nueva conexión a la base de datos
    LexppConfig.openNewDB("LexppScrapperConfig")

    # Cargamos códigos de asuntos
    LexppConfig.log_DEBUG("Cargando diccionario de asuntos...")
    LexppConfig.openNewCollection(targetCollection = "idExpedientes", targetDB = "LexppScrapperConfig")

    # Cargamos biblioteca de URL relevantes
    LexppConfig.log_DEBUG("Cargando biblioteca de url...")
    LexppConfig.openNewCollection(targetCollection = "urlBank", targetDB = "LexppScrapperConfig")

    # Cargamos biblioteca de funciones JS que vamos a usar
    LexppConfig.log_DEBUG("Cargando biblioteca de JS...")
    LexppConfig.openNewCollection(targetCollection = "jsBank", targetDB = "LexppScrapperConfig")

    return LexppConfig

# Función para guardar páginas
def logCurrentPage(modo: str, current, total):
    if not isinstance(modo, str):
        raise TypeError("El modo debe ser una cadena de texto")
    if modo not in ["todo", "tipoAsunto", "orgRadicacion", "ministro", "especifico"]:
        raise ValueError("El modo especificado no es válido!")

    # Obtenemos fecha y hora
    timeStamp = datetime.now()
    timeStampStr_1 = timeStamp.strftime("%Y-%d-%d")
    timeStampStr_2 = timeStamp.strftime("%H:%M:%S")

    # Definimos mensaje
    logMsg = "{0}|{1} de {2}".format(timeStampStr_2, current, total)

    # Escribimos el mensaje en el archivo
    with open("./logs/page_{0}_{1}.log".format(modo, timeStampStr_1), "a") as logFile:
        logFile.write(logMsg)

# Función para esperar que el loader desaparezca
def waitForLoader(scrapper: LexppScrapper, config: LexppConfig, timeOut = 30, onTimeOut = "retry"):
    if onTimeOut not in ["retry", "error"]:
        raise ValueError("Unknown value to parameter onTimeOut")

    # Log info
    config.log_INFO("Iniciando espera de carga de la página...")

    try:
        scrapper.waitUntil("ctl00_MainContentPlaceHolder_loadingPanelConsultaAsuntos", "id", timeOut, "invisibility_of_element_located")
    except (TimeoutError, ValueError) as e:
        # El usuario pidió volver a intentarlo en caso de error
        if onTimeOut == "retry":
            config.log_INFO("Ocurrió una excepción (tiempo excedido). Procediendo a reiniciar la espera...")
            return waitForLoader(scrapper, config, timeOut = timeOut, onTimeOut = "retry")
        # El usuario pidió mandar un error en caso de error
        elif onTimeOut == "error":
            config.log_CRITICAL("Ocurrió una excepción (tiempo excedido)")
            raise TimeoutError(e)
    else:
        # Si no ocurrió un error, mandamos True para romper la recursividad
        config.log_INFO("Espera terminada!")
        return True

# Rutina para escanear expedientes
def scanLoop(scrapper: LexppScrapper, config: LexppConfig, pageOption):
    # Iniciamos rutina
    # Primero recolectamos el número total de páginas
    totalPgCount = scrapper.getElement(element = "/html/body/div[1]/div/form/div[3]/div[2]/div[2]/table/tbody/tr[2]/td", findBy = "xpath")

    # El número de páginas viene en el formato "Página x de N", por lo que es necesario usar expresiones regulares
    totalPgCountTxt = totalPgCount.text
    totalPgCountRex = re.search(r"\D*(\d+)\D*(\d+)\D*", totalPgCountTxt)
    totalPgCountRex = totalPgCountRex.groups()[1]
    totalPgCountInt = int(totalPgCountRex)
    config.log_INFO("Hay {0} páginas de resultados".format(totalPgCountInt))

    # Guardamos el número de la página
    logCurrentPage(config.scrapperMode, pageOption, totalPgCountInt)

    # Inicializamos una variable que nos permita saber si podemos continuar
    continueState = True
    lastPage = False

    config.log_INFO("Entrando al loop de recolección...")
    while continueState:
        # Verificamos que no haya un loader activo
        waitForLoader(scrapper, config)

        # Recolectamos información sobre la página actual
        config.log_DEBUG("Buscando número de págin actual de resultados...")
        currentPg = scrapper.getElement(element = ".dxpCurrentPageNumber", findBy = "class name", multiple = True)
        currentPgTxt = currentPg[0].text
        currentPgRex = re.search(r"(\d+)", currentPgTxt)
        currentPgRex = currentPgRex.groups()[0]
        currentPgInt = int(currentPgRex)
        
        # Verificamos que la página actual esté dentro del rango
        if currentPgInt < totalPgCountInt:
            lastPage = False
        elif currentPgInt == totalPgCountInt:
            lastPage = True
        elif currentPgInt > totalPgCountInt:
            error_msg = "Hubo un error en la paginación (la página actual es mayor al total de páginas)"
            config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)
        
        # Log INFO
        config.log_INFO("Estamos en la página {0} de {1}".format(currentPgInt, totalPgCountInt))

        # Guardamos el número de la página
        logCurrentPage(config.scrapperMode, currentPgInt, totalPgCountInt)

        # Obtenemos los links con los expedientes
        expedientesLinks = scrapper.getElement(".dxgvControl a", "class name", True, False)

        # Iniciamos una operación por cada uno de los expedientes
        for linkElement in expedientesLinks:
            # Obtenemos el id de expediente
            idExpediente = linkElement.text
            # Limpiamos posibles espacios en blanco
            idExpediente = re.sub(r"\s+", "", idExpediente)
            # Obtenemos el id del asunto
            idAsunto = linkElement.get_attribute("href")
            idAsunto = idAsunto.split("=")[1]
            idAsunto = int(idAsunto)
            

            # Procedemos a obtener detalles del asunto
            
# Si el usuario quiere descargar por tipoAsunto
def getByAsuntoID(asuntoID, headlessOption, pageOption, LexppConfig):
    # Debug info
    LexppConfig.log_INFO("Obteniendo expedientes por ID de asunto...")

    # Guardamos en el objeto de configuración que estamos en el modo getByAsunto
    setattr(LexppConfig, "scrapperMode", "expedientes_byAsuntoID_{0}".format(asuntoID))

    # Rutina de inicializacion
    LexppConfig = init(LexppConfig)

    # Verificar que el tipo de asunto esté registrado
    LexppConfig.log_DEBUG("Verificando ID de asunto...")
    idQuery = LexppConfig.myCollections["LexppScrapperConfig/idExpedientes"].find_one({"id": asuntoID})
    if idQuery is None:
        error_msg = "El ID de asunto no está registrado!"
        LexppConfig.log_CRITICAL(error_msg)
        raise ValueError(error_msg)

    # Iniciamos nueva instancia del explorador web
    myScrapper = LexppScrapper(headless = False)

    # Navegamos a la URL (página de resultados de búsqueda de la SCJN)
    targetURL = LexppConfig.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "búsqueda"})
    targetURL = targetURL["formatted"]
    # Agregamos parámetros a la URL
    targetURL = targetURL.format("", 0, 0, asuntoID, 0, 0, 0, 0)

    # Navegamos a la URL
    myScrapper.goTo(targetURL)

    # Si el usuario pidió ir a una página en específico, iremos a esa página
    # Por default, el script empieza en la página 1
    if pageOption > 1:
        # Log info
        LexppConfig.log_INFO("El usuario solicitó iniciar su búsqueda en la página {0}...".format(pageOption))
        # Obtenemos JS correspondiente
        JSpayload = LexppConfig.myCollections["LexppScrapperConfig/jsBank"].find_one({"name": "goToPage"})
        if JSpayload is None:
            error_msg = "El JS no está registrado!"
            LexppConfig.log_CRITICAL(error_msg)
            raise ValueError(error_msg)
        # Configuramos payload
        JSpayload = JSpayload["payload"].format(pageOption)
        # Ejecutamos payload
        myScrapper.webdriver.execute_script(JSpayload)

        # Esperamos hasta que no haya un loader activo
        waitForLoader(myScrapper, LexppConfig)

    #Iniciamos el loop de recoleciión
    scanLoop(myScrapper, LexppConfig, pageOption)
    