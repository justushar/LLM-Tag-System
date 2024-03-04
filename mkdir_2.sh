#!/bin/bash

# Define the root directory where all PDF files will be moved
root_directory="/home/tusharbhatia/pyq-20240228T141016Z-001/pyq/2014-15/Even/ACC"

# Ensure the root directory exists
mkdir -p "$root_directory"

# Use find command to locate all PDF files in subdirectories and move them to the root directory
find . -name "*.pdf" -exec mv {} "$root_directory" \;

echo "PDF files moved to $root_directory"

