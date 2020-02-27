from LexppScrapper.LexppScrapper import LexppScrapper
from initConfig.config import LexppConfig

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

# Si el usuario quiere descargar por tipoAsunto
def getByAsuntoID(asuntoID, headlessOption, pageOption, LexppConfig):
    # Debug info
    LexppConfig.log_INFO("Obteniendo expedientes por ID de asunto...")

    # Inicializamos un dic global en el que guardaremos datos que leemos desde base de datos con configuraciones
    globalData = {}

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
        JSpayload = JSpayload.format(pageOption)

        # Esperamos hasta que no haya un loader activo
        waitForLoader(myScrapper, LexppConfig)
    