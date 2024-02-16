import requests
import json

# Define the endpoint URL
url = "http://localhost:11434/api/generate"
extracted_text = "END SEMESTER EXAMINATION : APRIL-MAY 2022 SOFTWARE ENGINEERING Time: 3 Hrs. Maximum Marks : 60"

# Define the data payload
data = {
    "model": "llama2",
    "prompt": f"Categorise the extracted text; {extracted_text} in the following categories. Respond using JSON Containing only the following fields :Subject Code:,Subject Name:, Semester:,Time:, Marks:. Semester is indicated by Month and Year",
    "format": "json",
    "stream": False
}

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
    
    # Save the formatted JSON to a file
    with open("formatted_response.json", "w") as f:
        f.write(formatted_response_data)
else:
    print("Error:", response.status_code)
