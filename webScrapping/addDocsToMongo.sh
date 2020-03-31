#!/bin/bash
#===============================================================================
# FILE: addDocsToMongo.sh
# DESCRIPTION: Agrega documentos obtenidos por los scripts de webScrapping a la base
#               de datos en MongoDB.
# AUTHOR: Pablo Reyes
#===============================================================================

# Some debug info
echo "Working directory: $0"
echo "Target directory: $1"
echo "Target library: $2"
echo "Target collection": $3

# Rename parameter
targetDir="$1"
targetLib="$2"
targetColl="$3"

# Get last character of target dir
lastChar="${targetDir: -1}"pñLexppScrapperConfig

# If last char equals "/" then leave targetDir as is, else, append slash
if [ "$lastChar" != "/" ]; then
    targetDir=$targetDir"/"
fi

# Append registered folder
registeredDir=$targetDir"registered/"

# Create folder
mkdir -p "$registeredDir"

# Define a for loop that process each file
N=4
for fileName in "$targetDir"*.json; do
    echo "Procesando '$fileName'..."
    echo "  > Agregando a MongoDB"
    # mongoimport --db LexppLibrary_SCJN --collection expedientes --file="$fileName"
    python3 /var/www/system/webScrapping/addDocsToMongo.py -f "$fileName" --library "$targetLib" --collection "$targetColl"
    echo "  > Moviendo a carpeta de archivos registrados..."
    # mv "$fileName" "$registeredDir"
    (( ++count % N == 0)) && wait
done
