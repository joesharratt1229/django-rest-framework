import requests

endpoint = "http://localhost:8000/api/" #server sends document and web browser reads that doc
get_response = requests.post(endpoint,
 json= {"title": "Abc123", "content": "Hello world", 
 "price": 20}) #get request

print(get_response.json())

 
