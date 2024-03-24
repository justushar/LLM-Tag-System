# Tesseract-NER README

## Introduction

This code utilizes Tesseract and Natural Language Recognition (NER) to extract text from a PDF file, categorize it into specific categories, and then send the categorized text to an API.

### Requirements

- Python 3.9+
- Tesseract OCR engine
- Pillow(pdf2image) library
- Pytesseract library
- Requests library
- Json library

### Prerequisites

Before running the script, ensure the following steps are completed:

1. Move all PDFs to one root folder (e.g., `./All`) using `mkdir_2.sh`.
2. Move the PDF files to directories having sequential numbers using `Mkdir.sh`.
   
   This ensures that the script can find and process the PDF files correctly.

### Usage

1. **Modify the `root_folder` variable:** Replace it with the actual path to your root folder.
2. **Modify the `stop_keywords` list:** If you want to halt OCR detection on specific keywords, add them to this list.
3. Run the script: `python FINAL.py`

### How the code works

1. **PDF to Images:** The script converts the PDF file into images and extracts text using Tesseract.
2. **Text Preprocessing:** The extracted text is processed to remove unnecessary characters and format it for the API.
3. **Category Extraction:** The script identifies the stop keywords and removes the lines containing them from the extracted text.
4. **API Submission:** The categorized text is sent to an API endpoint.
5. **Subfolder Processing:** The script can process multiple subfolders containing PDF files.
6. **JSON Processing:** The output from the API is returned as raw JSON and requires further processing. It is stored as `formatted_json` in the same directory as the script.

This ensures that the user is aware that the output from the API requires further processing.

### Note

- The script uses the `llama2` model from Tesseract.
- This code is designed to process a specific PDF file and categorize it based on the provided stop keywords.
- You may need to adjust the `stop_keywords` list based on the specific content of your PDF file.
- The script assumes that the Tesseract and Pillow libraries are installed.
- The script can be modified to process multiple PDF files in a directory.
