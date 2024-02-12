from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# Path to the Tesseract executable (update with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def preprocess_text(text):
    # Remove unnecessary characters and strip leading/trailing whitespaces
    return text.lower().strip()

def pdf_to_images(pdf_path, output_folder, stop_keywords=["Section A", "SECTION - A", "Section-A", "SECTION-A"]):
    # Get the base name of the PDF file (excluding the extension)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    images = convert_from_path(pdf_path)

    # Save the image with a filename indicating the page number
    image_filename = f"{pdf_name}-1.jpg"
    image_path = os.path.join(output_folder, image_filename)
    images[0].save(image_path)

    # OCR using Tesseract on the first page
    text_lines = pytesseract.image_to_string(images[0]).split('\n')

    for line_num, line in enumerate(text_lines):
        processed_line = preprocess_text(line)

        # Skip empty lines
        if not processed_line:
            continue

        print(f"{processed_line}")

        # Check for the stop keywords in each line
        if any(keyword.lower() in processed_line for keyword in stop_keywords):
            print(f"Stopping OCR detection at {stop_keywords} on page 1.")
            return

def process_subfolders(root_folder, stop_keywords):
    for subfolder_name in sorted(os.listdir(root_folder)):
        subfolder_path = os.path.join(root_folder, subfolder_name)

        if os.path.isdir(subfolder_path):
            # Get the PDF file in the subfolder
            pdf_files = [file for file in os.listdir(subfolder_path) if file.endswith(".pdf")]

            if pdf_files:
                pdf_path = os.path.join(subfolder_path, pdf_files[0])

                # Output folder will be the same as the subfolder
                output_folder = subfolder_path

                # Process the PDF file in the subfolder
                pdf_to_images(pdf_path, output_folder, stop_keywords)


if __name__ == "__main__":
    root_folder = "C:\\Chaitanya\\Tesseract-NER\\Tesseract-NER\\sanya-pyq"  # Replace with the root folder path
    stop_keywords = ["SECTION-A", "Section A", "SECTION - A", "Section-A"]  # Replace with the list of keywords to stop OCR detection
    process_subfolders(root_folder, stop_keywords)
