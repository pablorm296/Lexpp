from LexppScrapper.LexppScrapper import LexppScrapper
import logging
import datetime
import sys

#Definimos bitácora
logger = logging.getLogger(__name__)
#Definimos nivel de registro
logger.setLevel(logging.INFO)
#Definimos formato
logFormatter = logging.Formatter("%(levelname)-8s|%(asctime)s|%(module)s: %(message)s")
#Definimos handlers para consola y archivo
todayDate = datetime.date.today().strftime("%Y-%m-%d")
logFileHandler = logging.FileHandler("./logs/tesis_{0}.log".format(todayDate))
logFileHandler.setFormatter(logFormatter)
logConsoleHandler = logging.StreamHandler(sys.stdout)
logConsoleHandler.setFormatter(logFormatter)

#Nueva instancia de LexppScrapper
myScrapper = LexppScrapper(headless = False)