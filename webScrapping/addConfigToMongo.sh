#!/bin/bash
#===============================================================================
# FILE: addConfigToMongo.sh
# DESCRIPTION: Agrega archivos de configuración json a la base de datos y colección
#               correspondientes en MongoDB.
# AUTHOR: Pablo Reyes
#===============================================================================

# Diccionario de expedientes
mongoimport --db LexppScrapperConfig \
            --collection idExpedientes \
            --drop \
            --jsonArray \
            --file webScrapping/data/config/idExpedientes.json

# Diccionario de urls
mongoimport --db LexppScrapperConfig \
            --collection urlBank \
            --drop \
            --jsonArray \
            --file webScrapping/data/config/urlBank.json