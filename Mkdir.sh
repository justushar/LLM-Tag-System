#!/bin/bash

# Specify the directory where your files are located
sourceDirectory="/home/tusharbhatia/pyq-20240228T141016Z-001/pyq/2018-19/All"

# Get all files in the source directory
IFS=$'\n'  # Set internal field separator to newline to handle filenames with spaces correctly
files=$(find "$sourceDirectory" -type f -name "*.pdf")

# Initialize counter
counter=1

# Iterate through each file
for file in $files; do
    # Check if the file exists
    if [ -f "$file" ]; then
        # Create a directory with sequential numbering
        directoryName="$sourceDirectory/$counter"
        mkdir -p "$directoryName"

        # Move the file to the newly created directory
        mv "$file" "$directoryName"
        echo "Moved $file to $directoryName"

        # Increment counter
        ((counter++))
    else
        echo "File $file not found or inaccessible."
    fi
done
