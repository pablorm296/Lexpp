from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as WaitConditions
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotVisibleException, TimeoutException
import time
import logging

#Definimos bitácora
logger = logging.getLogger(__name__)

class LexppScrapper:
    #Inicialización (Crear webdriver)
    def __init__(self, headless = True, url = "https://www.google.com.mx"):
        #Verificamos parámetros
        if not isinstance(headless, bool):
            raise TypeError("'headless' must be a boolean object")
        #Inicializamos opciones
        self.webdriverOptions = FirefoxOptions()
        #Declaramos la opción headless
        self.webdriverOptions.headless = headless
        #Iniciamos nueva instancia del webdriver
        self.webdriver = webdriver.Firefox(options = self.webdriverOptions)
        #Vamos a la url especificada por el usuario 
        self.webdriver.get(url)
        #Enviamos mensajes de depuración
        logger.info("New LexppScrapper instance created at {0}".format(id(self)))
        logger.info("New Firefox driver created at {0}".format(id(self.webdriver)))
    
    #Reiniciar webdriver
    def restartWebDriver(self, headless = True, url = "https://www.google.com.mx"):
        #Verificamos parámetros
        if not isinstance(headless, bool):
            raise TypeError("'headless' must be a boolean object")
        #Matamos al webdriver
        self.webdriver.quit()
        #Reinicializamos opciones
        self.webdriverOptions = FirefoxOptions()
        #Redeclaramos la opción headless
        self.webdriverOptions.headless = True
        #Iniciamos nueva instancia del webdriver
        self.webdriver = webdriver.Firefox(options = self.webdriverOptions)
        #Vamos a la url especificada por el usuario 
        self.webdriver.get(url)
        #Enviamos mensajes de depuración
        logger.info("New Firefox driver created at {0}".format(id(self.webdriver)))

    #Cerrar el webdriver
    def killWebDriver(self):
        #Matamos al webdriver
        self.webdriver.quit()

    #Ir a la página
    def goTo(self, url):
        #Verificamos parámetros
        if not isinstance(url, str):
            raise TypeError("'url' must be a string object")
        #Vamos a la página
        self.webdriver.get(url)
    
    #Clic en el objeto
    def clickOn(self, element, findBy, continueOnExceptions = True):
        #Verificamos parámetros
        if not isinstance(element, str):
            raise TypeError("'url' must be a string object")
        if findBy not in ["name", "id", "xpath", "css selector", "class name"]:
            raise ValueError("'findBy' must be name, id or xpath")
        if not isinstance(continueOnExceptions, bool):
            raise TypeError("'continueOnExceptions' must be a bool object")
        #Buscamos elemento
        try:
            targetElem = self.__getSingleElement(element, findBy, continueOnExceptions)
        except NoSuchElementException as e:
            logger.warning("Exception while clicking: the specified element could not be found")
            if not continueOnExceptions:
                raise NoSuchElementException(e)
        else:
            #Le damos click al elemento
            try:
                targetElem.click()
            except ElementNotVisibleException as e:
                logger.warning("Exception while clicking: the specified element is not visible")
                if not continueOnExceptions:
                    raise ElementNotVisibleException(e)
            except ElementClickInterceptedException as e:
                logger.warning("Exception while clicking: the click action was intercepted")
                if not continueOnExceptions:
                    raise ElementClickInterceptedException(e)
            except Exception as e:
                logger.warning("Exception while clicking: unexpected error: {0}".format(e))
                if not continueOnExceptions:
                    raise
    
    #Obtener elemento
    def getElement(self, element, findBy, multiple = False, continueOnExceptions = True):
        #Verificamos parámetros
        if not isinstance(element, str):
            raise TypeError("'url' must be a string object")
        if findBy not in ["name", "id", "xpath", "css selector", "class name"]:
            raise ValueError("'findBy' must be name, id or xpath")
        if not isinstance(multiple, bool):
            raise TypeError("'multiple' must be a bool object")
        if not isinstance(continueOnExceptions, bool):
            raise TypeError("'continueOnExceptions' must be a bool object")
        #El usuario quiere uno o varios elementos
        if multiple:
            targetElem = self.__getMultipleElements(element, findBy, continueOnExceptions)
        else:
            targetElem = self.__getSingleElement(element, findBy, continueOnExceptions)
        
        return targetElem

    #Privativo: obtener varios elementos
    def __getSingleElement(self, element, findBy, continueOnExceptions):
        #Buscamos elemento
        try:
            targetElem = self.webdriver.find_element(findBy, element)
        except NoSuchElementException as e:
            logger.warning("Exception while locating element: the specified element could not be found")
            if not continueOnExceptions:
                raise NoSuchElementException(e)
            else:
                return None
        else:
            return targetElem
    #Privativo: obtener un solo elementos
    def __getMultipleElements(self, element, findBy, continueOnExceptions):
        #Buscamos elemento
        try:
            targetElem = self.webdriver.find_elements(findBy, element)
        except NoSuchElementException as e:
            logger.warning("Exception while locating element: the specified element could not be found")
            if not continueOnExceptions:
                raise NoSuchElementException(e)
            else:
                return None
        else:
            return targetElem

    #Esperar elemento
    def waitUntil(self, element, findBy, timeout = 20, condition = "element_to_be_clickable", ):
        #Verificamos argumentos
        if not isinstance(timeout, int):
            raise TypeError("'timeout' must be an integer object")
        if not isinstance(element, str):
            raise TypeError("'url' must be a string object")
        if findBy not in ["name", "id", "xpath", "css selector", "class name"]:
            raise ValueError("'findBy' must be name, id or xpath")
        if not isinstance(condition, str):
            raise TypeError("'condition' must be a string object")
        #Mensaje
        logging.info("User requested to wait for {0}({1},{2})".format(condition, findBy, element))
        #Definimos tipo de espera
        try:
            untilCondition = getattr(WaitConditions, condition)((findBy, element))
        except AttributeError as e:
            raise ValueError("Exception while waiting for element: unknown wait condition: {0}".format(e))
        #Iniciamos rutina de espera
        try:
            targetElem = WebDriverWait(self.webdriver, timeout).until(
                untilCondition
            )
        except TimeoutException as e:
            raise ValueError("Exception while waiting for element: timeout: {0}".format(e))
        else:
            logging.info("Wait condition fullfilled: {0}".format(targetElem.rect))
    
    #Esperar x segundos
    def sleep(self, seconds = 5):
        #Verificamos argumentos
        if not isinstance(seconds, int):
            raise TypeError("'seconds' must be an integer object")
        #Esperamos
        logging.info("User requested to wait for {0} seconds".format(seconds))
        time.sleep(5)
        logging.info("Wait condition fullfilled")
        