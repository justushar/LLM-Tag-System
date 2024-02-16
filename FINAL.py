from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import requests
import json

url = "http://127.0.0.1:11434/api/generate"


def response(extracted_text, output_folder):
    print(extracted_text)
    data = {
        "model": "llama2",
        "prompt": f"Categorise the extracted text; {extracted_text} in the following categories. Respond using JSON Containing only the following fields :Subject Code:,Subject Name:, Semester:,Time:, Marks:. Semester is indicated by Month and Year",
        "format": "json",
        "stream": False
    }
    print("Data to be sent to API:", data)  # Print the data dictionary before sending the request


    # Send the POST request
    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 200:
        # Parse the response JSON
        response_json = json.loads(response.content)

        # Extract the "response" field
        response_data = response_json.get("response", {})

        # Remove '\n' characters
        response_data_str = json.dumps(response_data)

        # Format JSON in human-readable format
        formatted_response_data = json.dumps(json.loads(response_data_str), indent=4)

        # Save the formatted JSON to a file in the same folder
        with open(os.path.join(output_folder, "formatted_response.json"), "w") as f:
            f.write(formatted_response_data)
    else:
        print("Error:", response.status_code)


def preprocess_text(text):
    # Remove unnecessary characters and strip leading/trailing whitespaces
    return text.lower().strip()
def pdf_to_images(pdf_path, output_folder, stop_keywords=["Section A", "SECTION - A", "Section-A", "SECTION-A", "note", "Note", "NOTE"]):
    # Get the base name of the PDF file (excluding the extension)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    images = convert_from_path(pdf_path)

    # Save the image with a filename indicating the page number
    image_filename = f"{pdf_name}-1.jpg"
    image_path = os.path.join(output_folder, image_filename)
    images[0].save(image_path)

    # Convert the image to grayscale
    grayscale_image = images[0].convert('L')

    # Crop the grayscale image to 50% of its height
    
    

    # OCR using Tesseract on the cropped grayscale image
    text = pytesseract.image_to_string(grayscale_image)

    # Initialize a variable to store the extracted text
    extracted_text = ""

    # Split the OCR result into lines
    text_lines = text.split('\n')

    for line in text_lines:
        processed_line = preprocess_text(line)

        # Skip empty lines
        if not processed_line:
            continue

        print(f"{processed_line}")

        # Append the processed line to the extracted text
        extracted_text += processed_line + "\n"

        # Check for the stop keywords in each line
        if any(keyword.lower() in processed_line for keyword in stop_keywords):
            # If the stop keyword is detected, remove the last appended line (which contains the stop keyword)
            extracted_text = extracted_text[:extracted_text.rfind(processed_line)]

            # Send the extracted text to the API
            response(extracted_text.strip(), output_folder)
            print(f"Stopping OCR detection at {stop_keywords} on page 1.")
            return

def process_subfolders(root_folder, stop_keywords):
    subfolder_count = 0
    for subfolder_name in sorted(os.listdir(root_folder)):
        subfolder_count += 1
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
    print(f"Number of subfolders accessed: {subfolder_count}")


if __name__ == "__main__":
    root_folder = "/home/tusharbhatia/Downloads/sanya-pyq-20240216T173747Z-001/sanya-pyq"  # Replace with the root folder path
    stop_keywords = ["SECTION-A", "Section A", "SECTION - A", "Section-A", "attempt", "Attempt", "ATTEMPT"]  # Replace with the list of keywords to stop OCR detection
    process_subfolders(root_folder, stop_keywords)
