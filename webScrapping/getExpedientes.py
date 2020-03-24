from LexppScrapper.LexppScrapper import LexppScrapper
from initConfig.config import LexppConfig
import getExpedientesMethods.getExpedientesMethods as getExpedientes
import argparse
import logging
import datetime

def main(arguments):

    # Convertir nivel de verbose
    if arguments.verbose == "debug":
        log_level = logging.DEBUG
    elif arguments.verbose == "normal":
        log_level = logging.INFO
    elif arguments.verbose == "none":
        log_level = logging.WARNING

    # Fecha del día de hoy (para el archivo de log)
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    # Inicializamos configuración
    myLexppConfig = LexppConfig(logFile = "./logs/expedientes_{0}.log".format(todayDate), logLevel = log_level, mode = arguments.modo, targetClient = 'mongodb://localhost:27017')

    # Dependiendo del tipo de modo, verificar que el usuario haya ingresado otros argumentos
    myLexppConfig.log_DEBUG("Verificando argumentos...")
    if arguments.modo == "tipoAsunto":
        # El ususario no puso el argumento necesario
        if arguments.tipoAsunto is None:
            error_msg = "Falta especificar el tipo de asunto!"
            myLexppConfig.log_CRITICAL(error_msg)
            raise TypeError(error_msg)
    elif arguments.modo == "orgRadicacion":
        # El ususario no puso el argumento necesario
        if arguments.orgRadicacion is None:
            error_msg = "Falta especificar el órgano de radicación!"
            myLexppConfig.log_CRITICAL(error_msg)
            raise TypeError(error_msg)
    elif arguments.modo == "ministro":
        # El ususario no puso el argumento necesario
        if arguments.ministro is None:
            error_msg = "Falta especificar el ministro!"
            myLexppConfig.log_CRITICAL(error_msg)
            raise TypeError(error_msg)
    elif arguments.modo == "especifico":
        # El ususario no puso el argumento necesario
        if arguments.expedienteInfo is None:
            error_msg = "Falta especificar ID de asunto o ID de expediente"
            myLexppConfig.log_CRITICAL(error_msg)
            raise TypeError(error_msg)

    # Activar modo
    if arguments.modo == "tipoAsunto":
        getExpedientes.getByAsuntoID(arguments.tipoAsunto, arguments.headless, arguments.goToPage, myLexppConfig)

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
    main(arguments)