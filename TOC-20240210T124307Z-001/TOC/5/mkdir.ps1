# Specify the directory where your files are located
$sourceDirectory = "H:\New folder (6)\TOC-20240210T124307Z-001\TOC"

# Get all files in the source directory
$files = Get-ChildItem -Path $sourceDirectory -File

# Initialize counter
$counter = 1

# Iterate through each file
foreach ($file in $files) {
    # Create a directory with sequential numbering
    $directoryName = Join-Path -Path $sourceDirectory -ChildPath $counter
    New-Item -Path $directoryName -ItemType Directory -Force

    # Move the file to the newly created directory
    Move-Item -Path $file.FullName -Destination $directoryName

    # Increment counter
    $counter++
}
