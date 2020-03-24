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
mkdir -p "$registeredDir"

# Define a loop that process each file
N=4
for filename in "$targetDir"*.json; do
    echo "$filename"
    (( ++count % N == 0)) && wait
done
