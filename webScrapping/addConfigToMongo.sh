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
            --file webScrapping/data/config/expedientes.json