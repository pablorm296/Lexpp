from LexppScrapper.LexppScrapper import LexppScrapper
from initConfig.config import LexppConfig
from datetime import datetime
import requests
import re
import uuid
import hashlib
import json
import time

# Clase para obtener detalles del Asunto
class Expediente:
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
        self.config.log_DEBUG("LexppId:{0}| LexppId_Expedientes:{1}".format(self.LexppId, self.LexppId_Expedientes))
        
        # Inicializamos el contenido y el esquema del expediente
        self.Content = dict()
        self.Schema = dict()
        
        # Empezamos a guardar el contenido del expediente
        self.getDetalleAsunto()
        self.getResolutivoGeneral()
        
        # Si existe resolutivo general, significa que podemos continuar extrayendo los datos
        foo_resolutivoGeneral = self.Content.get("resolutivoGeneral", None)
        foo_resolutivoGeneralData = foo_resolutivoGeneral.get("data", None)
        if foo_resolutivoGeneral is not None and foo_resolutivoGeneralData is not None:
            # Intentamos obtener el id de sesión
            try:
                self.sesionId = foo_resolutivoGeneral["data"][0].get("SesionID", None)
            except:
                self.sesionId = None
                config.log_INFO("El asunto {0} no tiene un id de sesión registrado".format(idAsunto))

            # Si hay ID de sesión podemos solicitar engroses, puntos resolutivos y votos
            if self.sesionId is not None:
                # Obtener engroses, puntos resolutivos y votos
                self.getEngrosePorAsuntoSesion()
                self.getPuntosResolutivos()
                self.getVotos()

        else:
            self.sesionId = None
            self.config.log_INFO("El asunto {0} aún no tiene resolutivo".format(idAsunto))

        # Obtenemos campos relevantes del expediente
        # Ver esquema de expedientes lexpp
        self.fillSchema()
        # Limpiamos los campos del esquema
        self.sanitizeSchema()

    # Función para descargar los documentos
    def downloadDocs(self, path, tipoAsuntoId):
        # Log info
        self.config.log_INFO("Descargando documentos...")
        
        # Log info
        self.config.log_INFO("Descargando engrose...")

        # Descargamos engroses
        engroseUrl = self.Schema.get("engroseUrl", None)
        if engroseUrl is not None:
            # Obtenemos extensión del archivo
            extension = engroseUrl.split(".")[-1]
            # Enviamos la solicitud
            engroseResponse = requests.get(engroseUrl, allow_redirects = True)
            # Obtenemos el encabezado de la respuesta
            engroseResponseHeaders = engroseResponse.headers
            # Verificamos el código de respuesta
            if (engroseResponse.status_code >= 400):
                warning_msg = "El servidor respondió con un error ({0}) al intentar descar un archivo de {1}".format(engroseResponse.status_code, engroseUrl)
                self.config.log_WARNING(warning_msg)
            # Verificamos el tipo del contenido
            engroseResponseContentType = engroseResponseHeaders.get("content-type", None)
            if 'text' in engroseResponseContentType.lower() or 'html' in engroseResponseContentType.lower():
                warning_msg = "El servidor respondió con un tipo de archivo inválido: {0}".format(engroseResponseContentType)
                self.config.log_WARNING(warning_msg)
            elif engroseResponseContentType is None:
                warning_msg = "Ocurrió un error al intentar leer la respuesta del servidor (conten-type is None)"
                self.config.log_WARNING(warning_msg)
            else:
                # Definir archivo objetivo
                targetPath = "{0}{1}_engrose.{2}".format(path, self.LexppId_Expedientes, extension)
                #Guardamos el archivo
                with open(targetPath, "wb") as targetFile:
                    targetFile.write(engroseResponse.content)
        else:
            warning_msg = "El expediente {0} no tiene un documento de engrose".format(self.idAsunto)
            self.config.log_WARNING(warning_msg)

        # Log info
        self.config.log_INFO("Descargando votos especiales...")

        # Descargar votos especiales
        votosEspecialesUrl = self.Schema.get("votosEspecialesUrl", None)
        if votosEspecialesUrl is not None and isinstance(votosEspecialesUrl, list):
            for i in range(len(votosEspecialesUrl)):
                votoEspecial = votosEspecialesUrl[i]
                # Obtenemos extensión del archivo
                extension = votoEspecial.split(".")[-1]
                # Enviamos la solicitud
                votoEspecialResponse = requests.get(votoEspecial, allow_redirects = True)
                # Obtenemos el encabezado de la respuesta
                votoEspecialResponseHeaders = votoEspecialResponse.headers
                # Verificamos el código de respuesta
                if (votoEspecialResponse.status_code >= 400):
                    warning_msg = "El servidor respondió con un error ({0}) al intentar descar un archivo de {1}".format(engroseResponse.status_code, engroseUrl)
                    self.config.log_WARNING(warning_msg)
                # Verificamos el tipo del contenido
                votoEspecialResponseContentType = votoEspecialResponseHeaders.get("content-type", None)
                if 'text' in votoEspecialResponseContentType.lower() or 'html' in votoEspecialResponseContentType.lower():
                    warning_msg = "El servidor respondió con un tipo de archivo inválido: {0}".format(engroseResponseContentType)
                    self.config.log_WARNING(warning_msg)
                elif votoEspecialResponseContentType is None:
                    warning_msg = "Ocurrió un error al intentar leer la respuesta del servidor (conten-type is None)"
                    self.config.log_WARNING(warning_msg)
                else:
                    # Definir archivo objetivo
                    targetPath = "{0}{2}_{3}_voto_{4}.{5}".format(path, tipoAsuntoId, self.LexppId_Expedientes, i, extension)
                    #Guardamos el archivo
                    with open(targetPath, "wb") as targetFile:
                        targetFile.write(engroseResponse.content)
        else:
            warning_msg = "El expediente {0} no tiene votos especiales".format(self.idAsunto)
            self.config.log_WARNING(warning_msg)

    def dump(self, path, tipoAsuntoId):
        # Log info
        self.config.log_INFO("Escribiendo información y contenido del expediente en disco...")
        # Definir archivo objetivo
        targetPath = "{0}{1}_dumped.json".format(path, self.LexppId_Expedientes)
        # Escribir contenidos
        with open(targetPath, "w") as targetFile:
            json.dump(self.Schema, targetFile)

        return True

    # Función para limpiar los campos de interés
    def sanitizeSchema(self):
        # Log info
        self.config.log_INFO("Limpiando campos de interés...")

        # Lista con las propiedades que son nombres propios
        nombresPropios = [
            "ministro",
            "secretarioProyectista",
            "secretarioAuxiliar",
            "ministroResolucion",
            "secretarioResolucion",
            "ministroVotosEspeciales"
        ]

        # Lista con las propiedades que son nombres de órganos
        organos = [
            "autoridades",
            "autoridadesContendientes",
            "promoventes"
            "organoOrigen"
        ]

        # Lista con las propiedades que son fechas
        fechas = [
            "fechaSesion",
            "fechaResolucionEngrose",
            "fechaRecepcion",
            "fechaTurnoMinistro",
            "fechaResolucion"
        ]

        # Iteramos por cada uno de los elementos en el esquema
        for key, value in self.Schema.items():
            # Si el valor es None, podemos saltarlo
            if value is None:
                continue
            # Si el valor es un string
            if isinstance(value, str):
                # Eliminar espacios en blanco al inicio y al final
                value = value.strip()
                # Eliminar apóstrofes
                value = re.sub(r"\'", "", value)
                # Convertimos en None las strings vacías
                if value == "": 
                    value = None
                    # Actualizamos y pasamos al siguiente elemento
                    self.Schema[key] = value
                    continue
                # Si no es una fecha
                if key not in fechas:
                    value = value.capitalize()
                # Si es un nombre propio
                if key in nombresPropios:
                    # Mayúsculas en la primera letra de cada palabra
                    value = value.title()
                    # Eliminar cosas que no son ni espacios ni letras
                    value = re.sub(r"[\W\d](?<!\s)", "", value)
                # Si es una fecha, intentar convertirla
                if key in fechas:
                    # Log info
                    self.config.log_INFO("Procesando fecha en {0}: {1} => {2}".format(self.idAsunto, key, value))
                    # Intentar convertirla de unix a humano
                    fooEpoch = re.search(r"Date\((-?\d+)\)", value, flags = re.I)
                    # Si es válido
                    if fooEpoch:
                        fooEpoch = fooEpoch.groups()[0]
                        fooEpoch = int(fooEpoch)/1000
                        fooEpoch = datetime.fromtimestamp(fooEpoch).isoformat()
                        value = fooEpoch
                    
                    # Intentar convertir formato de fecha estandar
                    fooTime = re.search(r"(\d+/\d+/\d+)", value, flags = re.I)
                    # Si es válido
                    if fooTime:
                        fooTime = fooTime.groups()[0]
                        fooTime = datetime.strptime(fooTime, "%d/%m/%Y").isoformat()
                        value = fooTime
            # Si es una lista
            if isinstance(value, list) and key in nombresPropios:
                for i in range(len(value)):
                    fooValue = value[i]
                    # Mayúsculas en la primera letra de cada palabra
                    fooValue = fooValue.title()
                    # Eliminar cosas que no son ni espacios ni letras
                    fooValue = re.sub(r"[\W\d](?<!\s)", "", fooValue)
                    value[i] = fooValue

        return True

    # Llena todos los campos de interés del expediente
    def fillSchema(self):
        # Log info
        self.config.log_INFO("Generando campos de interés...")

        # Abrir schema
        with open("/var/www/system/schemas/SCJN/expediente.schema.json") as jsonSchemaFile:
            jsonSchema = json.load(jsonSchemaFile)
        
        jsonSchemaProperties = jsonSchema["properties"]

        # Por cada propiedad en el esquema, agregarla al esquema del expediente
        for property in jsonSchemaProperties.keys():
            self.Schema.update({property: None})
        
        # Actualizar propiedades
        # Propiedades generales (ya están en self)
        self.Schema["rawContent"] = self.Content
        self.Schema["LexppId"] = self.LexppId
        self.Schema["Lexpp_expedientesId"] = self.LexppId_Expedientes
        self.Schema["asuntoId"] = self.idAsunto
        self.Schema["expedienteId"] = self.idExpediente

        # Propiedades que se obtienen del documento detalleAsunto
        self.Schema["tipoAsuntoId"] = self.detalleAsunto["data"].get("TipoAsuntoID", None)
        self.Schema["tipoAsunto"] = self.detalleAsunto["data"].get("TipoAsunto", None)
        self.Schema["pertenenecia"] = self.detalleAsunto["data"].get("Pertenencia", None)
        self.Schema["oficioId"] = self.detalleAsunto["data"].get("Oficio", None)
        self.Schema["estadoDelExpediente"] = self.detalleAsunto["data"].get("Estado", None)
        self.Schema["ministroId"] = self.detalleAsunto["data"].get("Ministro", None)
        self.Schema["ministro"] = None
        self.Schema["secretarioProyectista"] = self.detalleAsunto["data"].get("SecretarioProyectista", None)
        self.Schema["secretarioAuxiliar"] = self.detalleAsunto["data"].get("SecretarioAuxiliar", None)
        self.Schema["fechaRecepcion"] = self.detalleAsunto["data"].get("FechaRecepcion", None)
        self.Schema["fechaTurnoMinistro"] = self.detalleAsunto["data"].get("FechaTurnoMinistro", None)
        self.Schema["fechaResolucion"] = self.detalleAsunto["data"].get("FechaResolucion", None)
        self.Schema["actoReclamado"] = self.detalleAsunto["data"].get("ActoReclamado", None)
        self.Schema["autoridades"] = self.detalleAsunto["data"].get("Autoridades", None)
        self.Schema["autoridadesContendientes"] = self.detalleAsunto["data"].get("AutoridadesContendientes", None)
        self.Schema["promoventes"] = self.detalleAsunto["data"].get("Promoventes", None)
        self.Schema["area"] = self.detalleAsunto["data"].get("Area", None)
        self.Schema["tema"] = self.detalleAsunto["data"].get("Tema", None)
        self.Schema["temaLexpp"] = None
        self.Schema["temaFondo"] = self.detalleAsunto["data"].get("TemaFondo", None)
        self.Schema["resumenResolucion"] = self.detalleAsunto["data"].get("Resolucion", None)
        self.Schema["organoOrigen"] = self.detalleAsunto["data"].get("Organos", None)
        self.Schema["engroseUrl"] = self.detalleAsunto["data"].get("EngrosePublicoURL", None)
        self.Schema["votosEspecialesUrl"] = None
        self.Schema["ministroResolucionId"] = None

        # Propiedades que se obtienen del documento resolutivoGeneral
        # Primero verificamos que el contenido del resolutivo no esté vacío
        if len(self.resolutivoGeneral["data"]) > 0:
            self.Schema["ministroResolucion"] = self.resolutivoGeneral["data"][0].get("Ministro", None)
            self.Schema["secretarioResolucionId"] = self.resolutivoGeneral["data"][0].get("SecretarioID", None)
            self.Schema["secretarioResolucion"] = self.resolutivoGeneral["data"][0].get("Secretario", None)
            self.Schema["resolucionId"] = self.resolutivoGeneral["data"][0].get("SesionID", None)
            self.Schema["pertenenciaResolucionId"] = self.resolutivoGeneral["data"][0].get("PertenenciaID", None)
            self.Schema["pertenenciaResolucion"] = self.resolutivoGeneral["data"][0].get("Pertenencia", None)
            self.Schema["fechaSesion"] = self.resolutivoGeneral["data"][0].get("FechaSesion", None)
            self.Schema["fechaResolucionEngrose"] = self.resolutivoGeneral["data"][0].get("FechaResolucion", None)

        # Primero verificamos que el documento tenga una sesión de resolución
        if self.sesionId is not None:
            # Verificamos que existan puntos resolutivos
            if self.puntosResolutivos["data"] is not None:
                # Listas que se obtienen a partir del documento de puntos resolutivos
                # Definimos listas
                self.Schema["puntosResolutivos"] = list()
                self.Schema["votosPuntosResolutivos"] = list()
                # Llenamos listas
                for i in range(len(self.puntosResolutivos["data"])):
                    self.Schema["puntosResolutivos"].append(self.puntosResolutivos["data"][i].get("PuntoResolucion", None))
                    self.Schema["votosPuntosResolutivos"].append(self.puntosResolutivos["data"][i].get("Votacion", None))

            # Verificamos que existan puntos resolutivos
            if self.votos["data"] is not None:
                # Listas que se obtienen a partir del documento de votos
                self.Schema["ministroVotosEspeciales"] = list()
                self.Schema["ministroVotosEspecialesId"] = list()
                self.Schema["tipoVotosEspeciales"] = list()
                self.Schema["tipoVotosEspecialesId"] = list()
                self.Schema["votosEspecialesUrl"] = list()
                # Llenamos las listas
                for i in range(len(self.votos["data"])):
                    self.Schema["ministroVotosEspeciales"].append(self.votos["data"][i]["Ministros"])
                    self.Schema["ministroVotosEspecialesId"].append(self.votos["data"][i]["MinistroFirmaID"])
                    self.Schema["tipoVotosEspeciales"].append(self.votos["data"][i]["TipoVoto"])
                    self.Schema["tipoVotosEspecialesId"].append(self.votos["data"][i]["TipoVotoID"])
                    self.Schema["votosEspecialesUrl"].append(self.votos["data"][i]["URLInternet"])

        return True

    # Obtiene detalles del asunto
    def getDetalleAsunto(self):
        # Init empty doc in self
        self.detalleAsunto = None

        #Log info
        self.config.log_INFO("Obteniendo DetalleAsunto...")

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

        # Using index 0 to extract data from the list
        detalleAsunto = {"data": response_json_parsed[0], "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.detalleAsunto = detalleAsunto
        self.Content.update({"detalleAsunto": self.detalleAsunto})

        #Regresamos true
        return True

    # Obtiene resolutivo general
    def getResolutivoGeneral(self):
        # Init empty doc in self
        self.resolutivoGeneral = None

        # Log info
        self.config.log_INFO("Obteniendo resolutivoGeneral...")

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

    def getEngrosePorAsuntoSesion(self):
        # Init empty doc in self
        self.engrosePorAsuntoSesion = None

        # Log INFO
        self.config.log_INFO("Obteniendo EngrosePorAsuntoSesion...")

        # Obtenemos la url objetivo a partir de la base de datos
        targetUrl = self.config.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "obtieneEngrosePorAsuntoSesion"})
        # Verificamos que la URL esté registrada en la base de datos
        if targetUrl is None:
            error_msg = "La URL no está registrada!"
            self.config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)

        # Obtenemos la versión de la URL que puede formatearse con strings de python
        targetUrlFormatted = targetUrl["formatted"]

        # Creamos un objeto con los parámetros que vamos a enviar al servidor
        jsonPayload = {"pAsuntoID": self.idAsunto, "pRegistrosPagina": 5, "pSesionID": self.sesionId, "pStartRow": 0}

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

        #Regresamos respuesta
        engrosePorAsuntoSesion = {"data": response_json_parsed, "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.engrosePorAsuntoSesion = engrosePorAsuntoSesion
        self.Content.update({"engrosePorAsuntoSesion": self.engrosePorAsuntoSesion})

        return True

    def getPuntosResolutivos(self):
        # Init empty doc in self
        self.puntosResolutivos = None

        # Log INFO
        self.config.log_INFO("Obteniendo PuntosResolutivos...")

        # Obtenemos la url objetivo a partir de la base de datos
        targetUrl = self.config.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "obtienePuntosResolutivos"})
        # Verificamos que la URL esté registrada en la base de datos
        if targetUrl is None:
            error_msg = "La URL no está registrada!"
            self.config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)

        # Obtenemos la versión de la URL que puede formatearse con strings de python
        targetUrlFormatted = targetUrl["formatted"]

        # Creamos un objeto con los parámetros que vamos a enviar al servidor
        jsonPayload = {"pAsuntoID": self.idAsunto, "pRegistrosPagina": 5, "pSesionID": self.sesionId, "pStartRow": 0}

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

        #Regresamos respuesta
        puntosResolutivos = {"data": response_json_parsed, "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.puntosResolutivos = puntosResolutivos
        self.Content.update({"puntosResolutivos": self.puntosResolutivos})

        return True

    def getVotos(self):
        # Init empty doc in self
        self.votos = None

        # Log INFO
        self.config.log_INFO("Obteniendo Votos...")

        # Obtenemos la url objetivo a partir de la base de datos
        targetUrl = self.config.myCollections["LexppScrapperConfig/urlBank"].find_one({"name": "obtieneVotos"})
        # Verificamos que la URL esté registrada en la base de datos
        if targetUrl is None:
            error_msg = "La URL no está registrada!"
            self.config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)

        # Obtenemos la versión de la URL que puede formatearse con strings de python
        targetUrlFormatted = targetUrl["formatted"]

        # Creamos un objeto con los parámetros que vamos a enviar al servidor
        jsonPayload = {"pAsuntoID": self.idAsunto, "pRegistrosPagina": 5, "pSesionID": self.sesionId, "pStartRow": 0}

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

        #Regresamos respuesta
        votos = {"data": response_json_parsed, "md5": md5_encoder.hexdigest()}

        #Guardamos la respuesta
        self.votos = votos
        self.Content.update({"votos": self.votos})

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
def waitForLoader(scrapper: LexppScrapper, config: LexppConfig, padding = 2, timeOut = 30, onTimeOut = "retry"):
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
        # Esperamos el padding
        time.sleep(padding)

        return True

# Rutina para escanear expedientes
def scanLoop(scrapper: LexppScrapper, config: LexppConfig, pageOption, asuntoID):
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
        waitForLoader(scrapper, config, timeOut = 300)

        # Recolectamos información sobre la página actual
        config.log_DEBUG("Buscando número de págin actual de resultados...")
        currentPg = scrapper.getElement(element = "dxpCurrentPageNumber", findBy = "class name", multiple = True)
        currentPgTxt = currentPg[0].text
        currentPgRex = re.search(r"(\d+)", currentPgTxt)
        currentPgRex = currentPgRex.groups()[0]
        currentPgInt = int(currentPgRex)
        
        # Verificamos que la página actual esté dentro del rango
        if currentPgInt < totalPgCountInt:
            lastPage = False
        elif currentPgInt == totalPgCountInt:
            lastPage = True
            continueState = False
        elif currentPgInt > totalPgCountInt:
            error_msg = "Hubo un error en la paginación (la página actual es mayor al total de páginas)"
            config.log_CRITICAL(error_msg)
            raise ValueError(error_msg)
        
        # Log INFO
        config.log_INFO("Estamos en la página {0} de {1}".format(currentPgInt, totalPgCountInt))

        # Guardamos el número de la página
        logCurrentPage(config.scrapperMode, currentPgInt, totalPgCountInt)

        # Obtenemos los links con los expedientes
        expedientesLinks = scrapper.getElement("dxgvControl a", "class name", True, False)

        # Iniciamos una operación por cada uno de los expedientes
        for linkElement in expedientesLinks:
            # Verificamos que el link sea, efectivamente, a un expediente
            # Extraemos la propiedad aria-label
            ariaLabel = linkElement.get_attribute("aria-label")
            # Si es none, no lo es
            if ariaLabel is None:
                config.log_INFO("El elemento no es un expediente (no existe el atributo aria-label)!")
                continue
            # Verificar que la propiedad aria-label contenga algún de exto de nuestro interés
            ariaLabelMatch = re.match(r".*de\sexpediente.*", ariaLabel, re.IGNORECASE)
            if ariaLabelMatch is None:
                config.log_INFO("El elemento no es un expediente (el contenido de aria-label no es correcto: {0})!".format(ariaLabel))
                continue
            # Obtenemos el id de expediente
            idExpediente = linkElement.text
            # Limpiamos posibles espacios en blanco
            idExpediente = re.sub(r"\s+", "", idExpediente)
            # Obtenemos el id del asunto
            idAsunto = linkElement.get_attribute("href")
            idAsunto = idAsunto.split("=")[1]
            idAsunto = int(idAsunto)
            
            # Procedemos a obtener detalles del asunto
            fooExpediente = Expediente(idAsunto, idExpediente, config)

            # Descargamos documentos
            fooExpediente.downloadDocs("/var/www/db/SCJN/expedientes/docs/", tipoAsuntoId = asuntoID)
            # Guardamos información del expediente
            fooExpediente.dump("/var/www/db/SCJN/expedientes/", tipoAsuntoId = asuntoID)
        
        if lastPage:
            # Log info
            config.log_INFO("Esta es la última página de resultados. Fin de loop de recolección")
        else:
            # Log info
            config.log_INFO("Ejecutando js para avanzar a la siguiente página...")
            # Avanzamos a la siguiente página
            # Obtenemos JS correspondiente
            JSpayload = config.myCollections["LexppScrapperConfig/jsBank"].find_one({"name": "nextPage"})
            # Configuramos payload
            JSpayload = JSpayload["payload"]
            if JSpayload is None:
                error_msg = "El JS no está registrado!"
                config.log_CRITICAL(error_msg)
                raise ValueError(error_msg)
            # Ejecutamos payload
            scrapper.webdriver.execute_script(JSpayload)

            
# Si el usuario quiere descargar por tipoAsunto
def getByAsuntoID(asuntoID, headlessOption, pageOption, LexppConfig):
    # Debug info
    LexppConfig.log_INFO("Obteniendo expedientes por ID de asunto...")

    # Guardamos en el objeto de configuración que estamos en el modo getByAsunto
    setattr(LexppConfig, "scrapperMode", "tipoAsunto")
    setattr(LexppConfig, "scrapperModeComplete", "expedientes_byAsuntoID_{0}".format(asuntoID))

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
    if headlessOption == 0: 
        headlessOption = False 
    elif headlessOption == 1: 
        headlessOption = True
    myScrapper = LexppScrapper(headless = headlessOption)

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
    scanLoop(myScrapper, LexppConfig, pageOption, asuntoID)
    