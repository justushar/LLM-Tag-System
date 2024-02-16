# Tesseract Usage README

## Introduction

Welcome to the Tesseract Usage guide! Tesseract is an open-source Optical Character Recognition (OCR) engine maintained by Google. It is capable of recognizing text within images, making it a valuable tool for various applications such as document processing, text extraction, and more.

This README aims to provide you with a comprehensive overview of how to use Tesseract effectively.

## Installation

Before you can start using Tesseract, you need to install it on your system. Tesseract is available for installation on various platforms including Windows, macOS, and Linux. Here's how you can install it:

### Windows

```bash
# Install Tesseract using Chocolatey
choco install tesseract
```
otherwise it can be installed using the following link
```
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
```
### MAC OS
```
brew install tesseract
```
### LINUX
```
sudo apt-get install tesseract-ocr
```
```
Fedora: sudo dnf install tesseract-ocr
```
Installation can be checked using entering command tesseract in terminal.

## Python Package
Python offers Tesseract Wrapper as pytesseract. It can be installed using pip or conda.
```
pip install pytesseract
```
To perform operations on Images, we also require Pillow module.
```
pip install pillow
```
## First Steps
After installation. Clone the repository to read data from an Image using pytesseract module by using test.py file.

## Advanced Usage
Tesseract provides various options and configurations for better text recognition. You can specify language, page segmentation mode, output format, and more. Refer to the ![Tesseract documentation](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file) for detailed information on advanced usage.

## Tasks
1) Conversion of PDFs to JPGs and labelling them in serial number.
2) Extracting text (till section A) from JPG-1 using tesseract.
3) (a) Using Pattern Matching or (b) Using spAcy or LangChain, to categorize the extracted text.
4) Conversion of extracted text to json.