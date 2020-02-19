from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
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
        self.webdriverOptions.headless = True
        #Iniciamos nueva instancia del webdriver
        self.webdriver = webdriver.Firefox(options = self.webdriverOptions)
        #Vamos a la url especificada por el usuario 
        self.webdriver.get(url)
        #Enviamos mensajes de depuración
        logger.info("Nueva instancia de LexppScrapper iniciada en {0}".format(id(self)))
        logger.info("Nuevo webdriver Firefox iniciado en {0}".format(id(self.webdriver)))
    
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
        logger.info("Nuevo webdriver Firefox iniciado en {0}".format(id(self.webdriver)))

    #Cerrar el webdriver
    def killWebDriver(self):
        #Matamos al webdriver
        self.webdriver.quit()

    #Ir a la página
    def goTo(self, url):
        #Verificamos parámetros
        if not isinstance(url, str):
            raise TypeError("'url' must be a string object")
