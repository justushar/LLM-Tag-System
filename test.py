import pytesseract
from PIL import Image

def ocrimage(imagepath):
    # Open the image file
    with Image.open(imagepath) as img:
        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(img)
        return text

if __name__ == "__main__":
    # Example image path
    image_path = "test.jpg"

    # Perform OCR on the image
    extracted_text = ocrimage(image_path)

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)