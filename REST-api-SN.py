import requests

# ServiceNow API endpoint and credentials
url = "YOUR_REST_MESSAGE_ENDPOINT"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

# JSON payload for creating an Incident
incident_payload = {
    "short_description": "Incident Short Description",
    "description": "Incident Description",
    "caller_id": "User ID or Email",
    # Add more fields as needed
}

# Set up authentication
auth = (username, password)

# Send POST request to create an Incident
response = requests.post(url, json=incident_payload, auth=auth)

# Check response
if response.status_code == 201:
    print("Incident created successfully!")
    print("Incident Number:", response.json().get("number"))
else:
    print("Failed to create Incident:", response.text)