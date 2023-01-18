import requests

endpoint = "http://localhost:8000/api/products/1" #server sends document and web browser reads that doc
get_response = requests.get(endpoint) #

print(get_response.json())
