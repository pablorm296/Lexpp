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

# Rename parameter
targetDir=$1

# Get last character of target dir
lastChar="${targetDir: -1}"

# If last char equals "/" then leave targetDir as is, else, append slash
if [ "$lastChar" != "/" ]; then
    targetDir=$targetDir"/"
fi

# Append registered folder
registeredDir=$targetDir"registered/"

# Create folder
mkdir -p "$targetDir"

# Define a function that process each file
importDoc() {
    echo "$1"
}

# Export function
export -f importDoc

#Parallel
parallel importDoc ::: "$targetDir"
