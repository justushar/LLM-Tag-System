import pytesseract
from PIL import Image
import spacy
from spacy.matcher import Matcher

def categorize_text_from_image(image_path):
    # Use Tesseract to extract text from the image
    extracted_text = extract_text_from_image(image_path)
    
    # Categorize the extracted text
    categorized_results = categorize_text(extracted_text)
    
    return categorized_results

def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text

def categorize_text(extracted_text):
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    
    # Define pattern for time expressions
    time_pattern = [{"LIKE_NUM": True}, {"LOWER": {"IN": ["hrs", "hours"]}}]

    matcher.add("TIME", [time_pattern])

    doc = nlp(extracted_text)

    categories = {
        "Time": [],
        "Subject": [],
        "Semester period": []
    }

    matches = matcher(doc)
    for match_id, start, end in matches:
        if doc.vocab.strings[match_id] == "TIME":
            time_expression = doc[start:end].text
            categories["Time"].append(time_expression)

    for ent in doc.ents:
        if ent.label_ == "DATE":
            categories["Semester period"].append(ent.text)
        elif ent.label_ == "ORG" or ent.label_ == "PERSON":
            categories["Subject"].append(ent.text)

    return categories

if __name__ == "__main__":
    # Example image path
    image_path = "test.jpg"

    # Categorize text extracted from the image
    categorized_results = categorize_text_from_image(image_path)

    # Print the categorized results
    print("Categorized Results:")
    for category, values in categorized_results.items():
        print(f"{category}: {values}")
